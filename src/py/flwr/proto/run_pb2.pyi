"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import flwr.proto.fab_pb2
import flwr.proto.node_pb2
import flwr.proto.transport_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Run(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class OverrideConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> flwr.proto.transport_pb2.Scalar: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[flwr.proto.transport_pb2.Scalar] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    RUN_ID_FIELD_NUMBER: builtins.int
    FAB_ID_FIELD_NUMBER: builtins.int
    FAB_VERSION_FIELD_NUMBER: builtins.int
    OVERRIDE_CONFIG_FIELD_NUMBER: builtins.int
    FAB_HASH_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    fab_id: typing.Text
    fab_version: typing.Text
    @property
    def override_config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, flwr.proto.transport_pb2.Scalar]: ...
    fab_hash: typing.Text
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        fab_id: typing.Text = ...,
        fab_version: typing.Text = ...,
        override_config: typing.Optional[typing.Mapping[typing.Text, flwr.proto.transport_pb2.Scalar]] = ...,
        fab_hash: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fab_hash",b"fab_hash","fab_id",b"fab_id","fab_version",b"fab_version","override_config",b"override_config","run_id",b"run_id"]) -> None: ...
global___Run = Run

class RunStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int
    SUB_STATUS_FIELD_NUMBER: builtins.int
    DETAILS_FIELD_NUMBER: builtins.int
    status: typing.Text
    """"starting", "running", "finished" """

    sub_status: typing.Text
    """"completed", "failed", "stopped" or "" (non-finished)"""

    details: typing.Text
    """failure details"""

    def __init__(self,
        *,
        status: typing.Text = ...,
        sub_status: typing.Text = ...,
        details: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["details",b"details","status",b"status","sub_status",b"sub_status"]) -> None: ...
global___RunStatus = RunStatus

class CreateRunRequest(google.protobuf.message.Message):
    """CreateRun"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class OverrideConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> flwr.proto.transport_pb2.Scalar: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[flwr.proto.transport_pb2.Scalar] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    FAB_ID_FIELD_NUMBER: builtins.int
    FAB_VERSION_FIELD_NUMBER: builtins.int
    OVERRIDE_CONFIG_FIELD_NUMBER: builtins.int
    FAB_FIELD_NUMBER: builtins.int
    fab_id: typing.Text
    fab_version: typing.Text
    @property
    def override_config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, flwr.proto.transport_pb2.Scalar]: ...
    @property
    def fab(self) -> flwr.proto.fab_pb2.Fab: ...
    def __init__(self,
        *,
        fab_id: typing.Text = ...,
        fab_version: typing.Text = ...,
        override_config: typing.Optional[typing.Mapping[typing.Text, flwr.proto.transport_pb2.Scalar]] = ...,
        fab: typing.Optional[flwr.proto.fab_pb2.Fab] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fab",b"fab"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fab",b"fab","fab_id",b"fab_id","fab_version",b"fab_version","override_config",b"override_config"]) -> None: ...
global___CreateRunRequest = CreateRunRequest

class CreateRunResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id"]) -> None: ...
global___CreateRunResponse = CreateRunResponse

class GetRunRequest(google.protobuf.message.Message):
    """GetRun"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NODE_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    @property
    def node(self) -> flwr.proto.node_pb2.Node: ...
    run_id: builtins.int
    def __init__(self,
        *,
        node: typing.Optional[flwr.proto.node_pb2.Node] = ...,
        run_id: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["node",b"node"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["node",b"node","run_id",b"run_id"]) -> None: ...
global___GetRunRequest = GetRunRequest

class GetRunResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_FIELD_NUMBER: builtins.int
    @property
    def run(self) -> global___Run: ...
    def __init__(self,
        *,
        run: typing.Optional[global___Run] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["run",b"run"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["run",b"run"]) -> None: ...
global___GetRunResponse = GetRunResponse

class UpdateRunStatusRequest(google.protobuf.message.Message):
    """UpdateRunStatus"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    RUN_STATUS_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    @property
    def run_status(self) -> global___RunStatus: ...
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        run_status: typing.Optional[global___RunStatus] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["run_status",b"run_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id","run_status",b"run_status"]) -> None: ...
global___UpdateRunStatusRequest = UpdateRunStatusRequest

class UpdateRunStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___UpdateRunStatusResponse = UpdateRunStatusResponse

class GetRunStatusRequest(google.protobuf.message.Message):
    """GetRunStatus"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NODE_FIELD_NUMBER: builtins.int
    RUN_IDS_FIELD_NUMBER: builtins.int
    @property
    def node(self) -> flwr.proto.node_pb2.Node: ...
    @property
    def run_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        node: typing.Optional[flwr.proto.node_pb2.Node] = ...,
        run_ids: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["node",b"node"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["node",b"node","run_ids",b"run_ids"]) -> None: ...
global___GetRunStatusRequest = GetRunStatusRequest

class GetRunStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class RunStatusDictEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___RunStatus: ...
        def __init__(self,
            *,
            key: builtins.int = ...,
            value: typing.Optional[global___RunStatus] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    RUN_STATUS_DICT_FIELD_NUMBER: builtins.int
    @property
    def run_status_dict(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___RunStatus]: ...
    def __init__(self,
        *,
        run_status_dict: typing.Optional[typing.Mapping[builtins.int, global___RunStatus]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_status_dict",b"run_status_dict"]) -> None: ...
global___GetRunStatusResponse = GetRunStatusResponse

class GetPendingRunRequest(google.protobuf.message.Message):
    """GetPendingRun"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NODE_FIELD_NUMBER: builtins.int
    @property
    def node(self) -> flwr.proto.node_pb2.Node: ...
    def __init__(self,
        *,
        node: typing.Optional[flwr.proto.node_pb2.Node] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["node",b"node"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["node",b"node"]) -> None: ...
global___GetPendingRunRequest = GetPendingRunRequest

class GetPendingRunResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id"]) -> None: ...
global___GetPendingRunResponse = GetPendingRunResponse
