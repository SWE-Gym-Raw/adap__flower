#!/bin/bash
set -e
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../../

echo "=== test-tool.sh ==="

python -m isort --check-only framework/src/py/flwr_tool      && echo "- isort:  done" &&
python -m black --check framework/src/py/flwr_tool           && echo "- black:  done" &&
# mypy is covered by test.sh
python -m pylint framework/src/py/flwr_tool                  && echo "- pylint: done" &&
# python -m pytest -q framework/src/py/flwr_tool               && echo "- pytest: done" &&
echo "- All Python checks passed"
