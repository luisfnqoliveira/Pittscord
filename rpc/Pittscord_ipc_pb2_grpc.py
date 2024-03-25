# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import Pittscord_ipc_pb2 as Pittscord__ipc__pb2


class Pittscord_ipcStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetJSON = channel.unary_unary(
                '/Pittscord_ipc/GetJSON',
                request_serializer=Pittscord__ipc__pb2.JSONRequest.SerializeToString,
                response_deserializer=Pittscord__ipc__pb2.JSONResponse.FromString,
                )
        self.SayHello = channel.unary_unary(
                '/Pittscord_ipc/SayHello',
                request_serializer=Pittscord__ipc__pb2.HelloRequest.SerializeToString,
                response_deserializer=Pittscord__ipc__pb2.HelloResponse.FromString,
                )
        self.SendConfig = channel.unary_unary(
                '/Pittscord_ipc/SendConfig',
                request_serializer=Pittscord__ipc__pb2.ConfigRequest.SerializeToString,
                response_deserializer=Pittscord__ipc__pb2.ConfigResponse.FromString,
                )


class Pittscord_ipcServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetJSON(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Pittscord_ipcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetJSON': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJSON,
                    request_deserializer=Pittscord__ipc__pb2.JSONRequest.FromString,
                    response_serializer=Pittscord__ipc__pb2.JSONResponse.SerializeToString,
            ),
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=Pittscord__ipc__pb2.HelloRequest.FromString,
                    response_serializer=Pittscord__ipc__pb2.HelloResponse.SerializeToString,
            ),
            'SendConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SendConfig,
                    request_deserializer=Pittscord__ipc__pb2.ConfigRequest.FromString,
                    response_serializer=Pittscord__ipc__pb2.ConfigResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Pittscord_ipc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Pittscord_ipc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetJSON(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Pittscord_ipc/GetJSON',
            Pittscord__ipc__pb2.JSONRequest.SerializeToString,
            Pittscord__ipc__pb2.JSONResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Pittscord_ipc/SayHello',
            Pittscord__ipc__pb2.HelloRequest.SerializeToString,
            Pittscord__ipc__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Pittscord_ipc/SendConfig',
            Pittscord__ipc__pb2.ConfigRequest.SerializeToString,
            Pittscord__ipc__pb2.ConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
