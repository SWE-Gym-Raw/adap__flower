#!/bin/bash
set -e

case "$1" in
  rest)
    rest_arg="--rest"
    server_app_address="http://localhost:9091"
    server_address="http://localhost:9093"
    db_arg="--database :flwr-in-memory-state:"
    ;;
  sqlite)
    rest_arg=""
    server_address="127.0.0.1:9092"
    server_app_address="127.0.0.1:9091"
    db_arg="--database $(date +%s).db"
    ;;
  *)
    rest_arg=""
    server_address="127.0.0.1:9092"
    server_app_address="127.0.0.1:9091"
    db_arg="--database :flwr-in-memory-state:"
    ;;
esac

# Define the function
check_and_kill() {
  local pids=$1  # Get the PID as the first argument to the function
  for pid in $pids; do
    echo "Attempting to kill process ID: $pid"
    if kill "$pid" 2>/dev/null; then
        echo "Process $pid successfully killed."
    else
        echo "Failed to kill process $pid or it may have already terminated."
    fi
  done
}

# Install Flower app
pip install -e . --no-deps

# Remove any duplicates
sed -i '/^\[tool\.flwr\.federations\.e2e\]/,/^$/d' pyproject.toml

# Append the federations config to pyproject.toml
echo -e $"\n[tool.flwr.federations.e2e]\naddress = \"127.0.0.1:9093\"\ninsecure = true" >> pyproject.toml
sleep 1

echo "Starting SuperLink"
timeout 10m flower-superlink --insecure $db_arg $rest_arg &
sl_pids=$(pgrep -f "flower-superlink")
sleep 3

echo "Starting first client"
timeout 10m flower-supernode --insecure $rest_arg --superlink $server_address \
  --clientappio-api-address="localhost:9094" &
cl1_pid=$!
sleep 3

echo "Starting second client"
timeout 10m flower-supernode --insecure $rest_arg --superlink $server_address \
  --clientappio-api-address="localhost:9095" &
cl2_pid=$!
sleep 3

# Kill superlink, this should send the clients into their retry loops
echo "Killing Superlink"
check_and_kill "$sl_pids"
sleep 3

# Restart superlink, the clients should now be able to reconnect to it
echo "Restarting Superlink"
timeout 10m flower-superlink --insecure $db_arg $rest_arg 2>&1 | tee flwr_output.log &
sl_pids=$(pgrep -f "flower-superlink")
sleep 20

# Kill second client, this should send a DeleteNode message to the Superlink
echo "Killing second client"
check_and_kill "$cl1_pid"
sleep 5

# Starting new client, this is so we have enough clients to execute `flwr run`
echo "Starting new client"
timeout 10m flower-supernode --insecure $rest_arg --superlink $server_address \
  --clientappio-api-address "localhost:9094" &
cl1_pid=$!
sleep 5

# We execute `flwr run` to begin the training
echo "Executing flwr run to start training"
timeout 2m flwr run "." e2e &
sleep 10

# Kill first client as soon as the training starts, the flwr-serverapp should just 
# receive a failure in this case and continue the rounds when enough clients are 
# connected
echo "Killing first client"
check_and_kill "$cl1_pid"
sleep 3

# Restart first client so enough clients are connected to continue the FL rounds
echo "Starting new client"
timeout 5m flower-supernode --insecure $rest_arg --superlink $server_address \
  --clientappio-api-address "localhost:9094" &
cl1_pid=$!
sleep 5

# Initialize a flag to track if training is successful
found_success=false
timeout=120  # Timeout after 120 seconds
elapsed=0

# Check for "Success" in a loop with a timeout
while [ "$found_success" = false ] && [ $elapsed -lt $timeout ]; do
    if grep -q "Run finished" flwr_output.log; then
        echo "Training worked correctly!"
        found_success=true
        check_and_kill "$cl1_pid" "$cl2_pid"
        sleep 3
        check_and_kill "$sl_pids"
    else
        echo "Waiting for training ... ($elapsed seconds elapsed)"
    fi
    # Sleep for a short period and increment the elapsed time
    sleep 2
    elapsed=$((elapsed + 2))
done

if [ "$found_success" = false ]; then
    echo "Training had an issue and timed out."
    check_and_kill "$cl1_pid" "$cl2_pid"
    sleep 3
    check_and_kill "$sl_pids"
fi
