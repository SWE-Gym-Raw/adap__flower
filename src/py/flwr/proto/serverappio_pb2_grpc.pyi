"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import flwr.proto.fab_pb2
import flwr.proto.log_pb2
import flwr.proto.run_pb2
import flwr.proto.serverappio_pb2
import grpc

class ServerAppIoStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    CreateRun: grpc.UnaryUnaryMultiCallable[
        flwr.proto.run_pb2.CreateRunRequest,
        flwr.proto.run_pb2.CreateRunResponse]
    """Request run_id"""

    GetNodes: grpc.UnaryUnaryMultiCallable[
        flwr.proto.serverappio_pb2.GetNodesRequest,
        flwr.proto.serverappio_pb2.GetNodesResponse]
    """Return a set of nodes"""

    PushTaskIns: grpc.UnaryUnaryMultiCallable[
        flwr.proto.serverappio_pb2.PushTaskInsRequest,
        flwr.proto.serverappio_pb2.PushTaskInsResponse]
    """Create one or more tasks"""

    PullTaskRes: grpc.UnaryUnaryMultiCallable[
        flwr.proto.serverappio_pb2.PullTaskResRequest,
        flwr.proto.serverappio_pb2.PullTaskResResponse]
    """Get task results"""

    GetRun: grpc.UnaryUnaryMultiCallable[
        flwr.proto.run_pb2.GetRunRequest,
        flwr.proto.run_pb2.GetRunResponse]
    """Get run details"""

    GetFab: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fab_pb2.GetFabRequest,
        flwr.proto.fab_pb2.GetFabResponse]
    """Get FAB"""

    PullServerAppInputs: grpc.UnaryUnaryMultiCallable[
        flwr.proto.serverappio_pb2.PullServerAppInputsRequest,
        flwr.proto.serverappio_pb2.PullServerAppInputsResponse]
    """Pull ServerApp inputs"""

    PushServerAppOutputs: grpc.UnaryUnaryMultiCallable[
        flwr.proto.serverappio_pb2.PushServerAppOutputsRequest,
        flwr.proto.serverappio_pb2.PushServerAppOutputsResponse]
    """Push ServerApp outputs"""

    UpdateRunStatus: grpc.UnaryUnaryMultiCallable[
        flwr.proto.run_pb2.UpdateRunStatusRequest,
        flwr.proto.run_pb2.UpdateRunStatusResponse]
    """Update the status of a given run"""

    PushLogs: grpc.UnaryUnaryMultiCallable[
        flwr.proto.log_pb2.PushLogsRequest,
        flwr.proto.log_pb2.PushLogsResponse]
    """Push ServerApp logs"""


class ServerAppIoServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateRun(self,
        request: flwr.proto.run_pb2.CreateRunRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.run_pb2.CreateRunResponse:
        """Request run_id"""
        pass

    @abc.abstractmethod
    def GetNodes(self,
        request: flwr.proto.serverappio_pb2.GetNodesRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.serverappio_pb2.GetNodesResponse:
        """Return a set of nodes"""
        pass

    @abc.abstractmethod
    def PushTaskIns(self,
        request: flwr.proto.serverappio_pb2.PushTaskInsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.serverappio_pb2.PushTaskInsResponse:
        """Create one or more tasks"""
        pass

    @abc.abstractmethod
    def PullTaskRes(self,
        request: flwr.proto.serverappio_pb2.PullTaskResRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.serverappio_pb2.PullTaskResResponse:
        """Get task results"""
        pass

    @abc.abstractmethod
    def GetRun(self,
        request: flwr.proto.run_pb2.GetRunRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.run_pb2.GetRunResponse:
        """Get run details"""
        pass

    @abc.abstractmethod
    def GetFab(self,
        request: flwr.proto.fab_pb2.GetFabRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.fab_pb2.GetFabResponse:
        """Get FAB"""
        pass

    @abc.abstractmethod
    def PullServerAppInputs(self,
        request: flwr.proto.serverappio_pb2.PullServerAppInputsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.serverappio_pb2.PullServerAppInputsResponse:
        """Pull ServerApp inputs"""
        pass

    @abc.abstractmethod
    def PushServerAppOutputs(self,
        request: flwr.proto.serverappio_pb2.PushServerAppOutputsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.serverappio_pb2.PushServerAppOutputsResponse:
        """Push ServerApp outputs"""
        pass

    @abc.abstractmethod
    def UpdateRunStatus(self,
        request: flwr.proto.run_pb2.UpdateRunStatusRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.run_pb2.UpdateRunStatusResponse:
        """Update the status of a given run"""
        pass

    @abc.abstractmethod
    def PushLogs(self,
        request: flwr.proto.log_pb2.PushLogsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.log_pb2.PushLogsResponse:
        """Push ServerApp logs"""
        pass


def add_ServerAppIoServicer_to_server(servicer: ServerAppIoServicer, server: grpc.Server) -> None: ...
