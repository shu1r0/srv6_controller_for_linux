# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import srv6_route_pb2 as srv6__route__pb2


class Seg6ServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddRoute = channel.unary_unary(
                '/Seg6Service/AddRoute',
                request_serializer=srv6__route__pb2.Seg6RouteRequest.SerializeToString,
                response_deserializer=srv6__route__pb2.Seg6RouteReply.FromString,
                )
        self.RemoveRoute = channel.unary_unary(
                '/Seg6Service/RemoveRoute',
                request_serializer=srv6__route__pb2.Seg6RouteRequest.SerializeToString,
                response_deserializer=srv6__route__pb2.Seg6RouteReply.FromString,
                )
        self.ShowRoute = channel.unary_unary(
                '/Seg6Service/ShowRoute',
                request_serializer=srv6__route__pb2.ShowRoutes6Request.SerializeToString,
                response_deserializer=srv6__route__pb2.ShowRoutes6Reply.FromString,
                )


class Seg6ServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddRoute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveRoute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShowRoute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Seg6ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.AddRoute,
                    request_deserializer=srv6__route__pb2.Seg6RouteRequest.FromString,
                    response_serializer=srv6__route__pb2.Seg6RouteReply.SerializeToString,
            ),
            'RemoveRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveRoute,
                    request_deserializer=srv6__route__pb2.Seg6RouteRequest.FromString,
                    response_serializer=srv6__route__pb2.Seg6RouteReply.SerializeToString,
            ),
            'ShowRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.ShowRoute,
                    request_deserializer=srv6__route__pb2.ShowRoutes6Request.FromString,
                    response_serializer=srv6__route__pb2.ShowRoutes6Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Seg6Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Seg6Service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Seg6Service/AddRoute',
            srv6__route__pb2.Seg6RouteRequest.SerializeToString,
            srv6__route__pb2.Seg6RouteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Seg6Service/RemoveRoute',
            srv6__route__pb2.Seg6RouteRequest.SerializeToString,
            srv6__route__pb2.Seg6RouteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShowRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Seg6Service/ShowRoute',
            srv6__route__pb2.ShowRoutes6Request.SerializeToString,
            srv6__route__pb2.ShowRoutes6Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)