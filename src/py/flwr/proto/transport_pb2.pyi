"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Code:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _CodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Code.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _Code.ValueType  # 0
    GET_PROPERTIES_NOT_IMPLEMENTED: _Code.ValueType  # 1
    GET_PARAMETERS_NOT_IMPLEMENTED: _Code.ValueType  # 2
    FIT_NOT_IMPLEMENTED: _Code.ValueType  # 3
    EVALUATE_NOT_IMPLEMENTED: _Code.ValueType  # 4
class Code(_Code, metaclass=_CodeEnumTypeWrapper):
    pass

OK: Code.ValueType  # 0
GET_PROPERTIES_NOT_IMPLEMENTED: Code.ValueType  # 1
GET_PARAMETERS_NOT_IMPLEMENTED: Code.ValueType  # 2
FIT_NOT_IMPLEMENTED: Code.ValueType  # 3
EVALUATE_NOT_IMPLEMENTED: Code.ValueType  # 4
global___Code = Code


class _Reason:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ReasonEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Reason.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _Reason.ValueType  # 0
    RECONNECT: _Reason.ValueType  # 1
    POWER_DISCONNECTED: _Reason.ValueType  # 2
    WIFI_UNAVAILABLE: _Reason.ValueType  # 3
    ACK: _Reason.ValueType  # 4
class Reason(_Reason, metaclass=_ReasonEnumTypeWrapper):
    pass

UNKNOWN: Reason.ValueType  # 0
RECONNECT: Reason.ValueType  # 1
POWER_DISCONNECTED: Reason.ValueType  # 2
WIFI_UNAVAILABLE: Reason.ValueType  # 3
ACK: Reason.ValueType  # 4
global___Reason = Reason


class Status(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code: global___Code.ValueType
    message: typing.Text
    def __init__(self,
        *,
        code: global___Code.ValueType = ...,
        message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code",b"code","message",b"message"]) -> None: ...
global___Status = Status

class Parameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TENSORS_FIELD_NUMBER: builtins.int
    TENSOR_TYPE_FIELD_NUMBER: builtins.int
    @property
    def tensors(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    tensor_type: typing.Text
    def __init__(self,
        *,
        tensors: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        tensor_type: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tensor_type",b"tensor_type","tensors",b"tensors"]) -> None: ...
global___Parameters = Parameters

class ServerMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ReconnectIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        SECONDS_FIELD_NUMBER: builtins.int
        seconds: builtins.int
        def __init__(self,
            *,
            seconds: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["seconds",b"seconds"]) -> None: ...

    class GetPropertiesIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        CONFIG_FIELD_NUMBER: builtins.int
        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            config: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config"]) -> None: ...

    class GetParametersIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        CONFIG_FIELD_NUMBER: builtins.int
        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            config: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config"]) -> None: ...

    class FitIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        PARAMETERS_FIELD_NUMBER: builtins.int
        CONFIG_FIELD_NUMBER: builtins.int
        @property
        def parameters(self) -> global___Parameters: ...
        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            parameters: typing.Optional[global___Parameters] = ...,
            config: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config","parameters",b"parameters"]) -> None: ...

    class EvaluateIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        PARAMETERS_FIELD_NUMBER: builtins.int
        CONFIG_FIELD_NUMBER: builtins.int
        @property
        def parameters(self) -> global___Parameters: ...
        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            parameters: typing.Optional[global___Parameters] = ...,
            config: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config","parameters",b"parameters"]) -> None: ...

    RECONNECT_INS_FIELD_NUMBER: builtins.int
    GET_PROPERTIES_INS_FIELD_NUMBER: builtins.int
    GET_PARAMETERS_INS_FIELD_NUMBER: builtins.int
    FIT_INS_FIELD_NUMBER: builtins.int
    EVALUATE_INS_FIELD_NUMBER: builtins.int
    @property
    def reconnect_ins(self) -> global___ServerMessage.ReconnectIns: ...
    @property
    def get_properties_ins(self) -> global___ServerMessage.GetPropertiesIns: ...
    @property
    def get_parameters_ins(self) -> global___ServerMessage.GetParametersIns: ...
    @property
    def fit_ins(self) -> global___ServerMessage.FitIns: ...
    @property
    def evaluate_ins(self) -> global___ServerMessage.EvaluateIns: ...
    def __init__(self,
        *,
        reconnect_ins: typing.Optional[global___ServerMessage.ReconnectIns] = ...,
        get_properties_ins: typing.Optional[global___ServerMessage.GetPropertiesIns] = ...,
        get_parameters_ins: typing.Optional[global___ServerMessage.GetParametersIns] = ...,
        fit_ins: typing.Optional[global___ServerMessage.FitIns] = ...,
        evaluate_ins: typing.Optional[global___ServerMessage.EvaluateIns] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["evaluate_ins",b"evaluate_ins","fit_ins",b"fit_ins","get_parameters_ins",b"get_parameters_ins","get_properties_ins",b"get_properties_ins","msg",b"msg","reconnect_ins",b"reconnect_ins"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["evaluate_ins",b"evaluate_ins","fit_ins",b"fit_ins","get_parameters_ins",b"get_parameters_ins","get_properties_ins",b"get_properties_ins","msg",b"msg","reconnect_ins",b"reconnect_ins"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["msg",b"msg"]) -> typing.Optional[typing_extensions.Literal["reconnect_ins","get_properties_ins","get_parameters_ins","fit_ins","evaluate_ins"]]: ...
global___ServerMessage = ServerMessage

class ClientMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class DisconnectRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        REASON_FIELD_NUMBER: builtins.int
        reason: global___Reason.ValueType
        def __init__(self,
            *,
            reason: global___Reason.ValueType = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["reason",b"reason"]) -> None: ...

    class GetPropertiesRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class PropertiesEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        STATUS_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        @property
        def status(self) -> global___Status: ...
        @property
        def properties(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            status: typing.Optional[global___Status] = ...,
            properties: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["status",b"status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["properties",b"properties","status",b"status"]) -> None: ...

    class GetParametersRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        STATUS_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        @property
        def status(self) -> global___Status: ...
        @property
        def parameters(self) -> global___Parameters: ...
        def __init__(self,
            *,
            status: typing.Optional[global___Status] = ...,
            parameters: typing.Optional[global___Parameters] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters","status",b"status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["parameters",b"parameters","status",b"status"]) -> None: ...

    class FitRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class MetricsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        STATUS_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        NUM_EXAMPLES_FIELD_NUMBER: builtins.int
        METRICS_FIELD_NUMBER: builtins.int
        @property
        def status(self) -> global___Status: ...
        @property
        def parameters(self) -> global___Parameters: ...
        num_examples: builtins.int
        @property
        def metrics(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            status: typing.Optional[global___Status] = ...,
            parameters: typing.Optional[global___Parameters] = ...,
            num_examples: builtins.int = ...,
            metrics: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters","status",b"status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["metrics",b"metrics","num_examples",b"num_examples","parameters",b"parameters","status",b"status"]) -> None: ...

    class EvaluateRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class MetricsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        STATUS_FIELD_NUMBER: builtins.int
        LOSS_FIELD_NUMBER: builtins.int
        NUM_EXAMPLES_FIELD_NUMBER: builtins.int
        METRICS_FIELD_NUMBER: builtins.int
        @property
        def status(self) -> global___Status: ...
        loss: builtins.float
        num_examples: builtins.int
        @property
        def metrics(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            status: typing.Optional[global___Status] = ...,
            loss: builtins.float = ...,
            num_examples: builtins.int = ...,
            metrics: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["status",b"status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["loss",b"loss","metrics",b"metrics","num_examples",b"num_examples","status",b"status"]) -> None: ...

    DISCONNECT_RES_FIELD_NUMBER: builtins.int
    GET_PROPERTIES_RES_FIELD_NUMBER: builtins.int
    GET_PARAMETERS_RES_FIELD_NUMBER: builtins.int
    FIT_RES_FIELD_NUMBER: builtins.int
    EVALUATE_RES_FIELD_NUMBER: builtins.int
    @property
    def disconnect_res(self) -> global___ClientMessage.DisconnectRes: ...
    @property
    def get_properties_res(self) -> global___ClientMessage.GetPropertiesRes: ...
    @property
    def get_parameters_res(self) -> global___ClientMessage.GetParametersRes: ...
    @property
    def fit_res(self) -> global___ClientMessage.FitRes: ...
    @property
    def evaluate_res(self) -> global___ClientMessage.EvaluateRes: ...
    def __init__(self,
        *,
        disconnect_res: typing.Optional[global___ClientMessage.DisconnectRes] = ...,
        get_properties_res: typing.Optional[global___ClientMessage.GetPropertiesRes] = ...,
        get_parameters_res: typing.Optional[global___ClientMessage.GetParametersRes] = ...,
        fit_res: typing.Optional[global___ClientMessage.FitRes] = ...,
        evaluate_res: typing.Optional[global___ClientMessage.EvaluateRes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disconnect_res",b"disconnect_res","evaluate_res",b"evaluate_res","fit_res",b"fit_res","get_parameters_res",b"get_parameters_res","get_properties_res",b"get_properties_res","msg",b"msg"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["disconnect_res",b"disconnect_res","evaluate_res",b"evaluate_res","fit_res",b"fit_res","get_parameters_res",b"get_parameters_res","get_properties_res",b"get_properties_res","msg",b"msg"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["msg",b"msg"]) -> typing.Optional[typing_extensions.Literal["disconnect_res","get_properties_res","get_parameters_res","fit_res","evaluate_res"]]: ...
global___ClientMessage = ClientMessage

class Scalar(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOUBLE_FIELD_NUMBER: builtins.int
    UINT64_FIELD_NUMBER: builtins.int
    SINT64_FIELD_NUMBER: builtins.int
    BOOL_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    double: builtins.float
    uint64: builtins.int
    """float float = 2;
    int32 int32 = 3;
    int64 int64 = 4;
    uint32 uint32 = 5;
    """

    sint64: builtins.int
    """sint32 sint32 = 7;"""

    bool: builtins.bool
    """fixed32 fixed32 = 9;
    fixed64 fixed64 = 10;
    sfixed32 sfixed32 = 11;
    sfixed64 sfixed64 = 12;
    """

    string: typing.Text
    bytes: builtins.bytes
    def __init__(self,
        *,
        double: builtins.float = ...,
        uint64: builtins.int = ...,
        sint64: builtins.int = ...,
        bool: builtins.bool = ...,
        string: typing.Text = ...,
        bytes: builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bool",b"bool","bytes",b"bytes","double",b"double","scalar",b"scalar","sint64",b"sint64","string",b"string","uint64",b"uint64"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bool",b"bool","bytes",b"bytes","double",b"double","scalar",b"scalar","sint64",b"sint64","string",b"string","uint64",b"uint64"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["scalar",b"scalar"]) -> typing.Optional[typing_extensions.Literal["double","uint64","sint64","bool","string","bytes"]]: ...
global___Scalar = Scalar
