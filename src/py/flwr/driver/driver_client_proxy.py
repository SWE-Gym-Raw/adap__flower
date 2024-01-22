# Copyright 2020 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Flower ClientProxy implementation for Driver API."""


import time
from typing import Optional, cast

from flwr import common
from flwr.common import serde
from flwr.proto.node_pb2 import Node  # pylint: disable=E0611
from flwr.proto.task_pb2 import Task, TaskIns  # pylint: disable=E0611
from flwr.proto.transport_pb2 import (  # pylint: disable=E0611
    ClientMessage,
    ServerMessage,
)
from flwr.server.client_proxy import ClientProxy

from .driver import Driver

SLEEP_TIME = 1


class DriverClientProxy(ClientProxy):
    """Flower client proxy which delegates work using the Driver API."""

    def __init__(self, node_id: int, driver: Driver, anonymous: bool):
        super().__init__(str(node_id))
        self.node_id = node_id
        self.driver = driver
        self.anonymous = anonymous

    def get_properties(
        self, ins: common.GetPropertiesIns, timeout: Optional[float]
    ) -> common.GetPropertiesRes:
        """Return client's properties."""
        server_message_proto: ServerMessage = serde.server_message_to_proto(
            server_message=common.ServerMessage(get_properties_ins=ins)
        )
        return cast(
            common.GetPropertiesRes,
            self._send_receive_msg(server_message_proto, timeout).get_properties_res,
        )

    def get_parameters(
        self, ins: common.GetParametersIns, timeout: Optional[float]
    ) -> common.GetParametersRes:
        """Return the current local model parameters."""
        server_message_proto: ServerMessage = serde.server_message_to_proto(
            server_message=common.ServerMessage(get_parameters_ins=ins)
        )
        return cast(
            common.GetParametersRes,
            self._send_receive_msg(server_message_proto, timeout).get_parameters_res,
        )

    def fit(self, ins: common.FitIns, timeout: Optional[float]) -> common.FitRes:
        """Train model parameters on the locally held dataset."""
        server_message_proto: ServerMessage = serde.server_message_to_proto(
            server_message=common.ServerMessage(fit_ins=ins)
        )
        return cast(
            common.FitRes,
            self._send_receive_msg(server_message_proto, timeout).fit_res,
        )

    def evaluate(
        self, ins: common.EvaluateIns, timeout: Optional[float]
    ) -> common.EvaluateRes:
        """Evaluate model parameters on the locally held dataset."""
        server_message_proto: ServerMessage = serde.server_message_to_proto(
            server_message=common.ServerMessage(evaluate_ins=ins)
        )
        return cast(
            common.EvaluateRes,
            self._send_receive_msg(server_message_proto, timeout).evaluate_res,
        )

    def reconnect(
        self, ins: common.ReconnectIns, timeout: Optional[float]
    ) -> common.DisconnectRes:
        """Disconnect and (optionally) reconnect later."""
        return common.DisconnectRes(reason="")  # Nothing to do here (yet)

    def _send_receive_msg(
        self, server_message: ServerMessage, timeout: Optional[float]
    ) -> ClientMessage:
        task_ins = TaskIns(
            task=Task(
                producer=Node(
                    node_id=0,
                    anonymous=True,
                ),
                consumer=Node(
                    node_id=self.node_id,
                    anonymous=self.anonymous,
                ),
                legacy_server_message=server_message,
            ),
        )

        # Send TaskIns to Driver API
        task_ids = self.driver.push_task_ins([task_ins])

        if len(task_ids) != 1:
            raise ValueError("Unexpected number of task_ids")

        task_id = task_ids[0]
        if task_id == "":
            raise ValueError(f"Failed to schedule task for node {self.node_id}")

        if timeout:
            start_time = time.time()

        while True:
            # Ask Driver API for TaskRes
            task_res_list = self.driver.pull_task_res([task_id])

            if len(task_res_list) == 1:
                task_res = task_res_list[0]
                return serde.client_message_from_proto(  # type: ignore
                    task_res.task.legacy_client_message
                )

            if timeout is not None and time.time() > start_time + timeout:
                raise RuntimeError("Timeout reached")
            time.sleep(SLEEP_TIME)
