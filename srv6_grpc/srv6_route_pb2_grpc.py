# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import srv6_route_pb2 as srv6__route__pb2


class Seg6ServiceStub(object):
    """*
    Route Service on Agent
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddRoute = channel.unary_unary(
                '/Seg6Service/AddRoute',
                request_serializer=srv6__route__pb2.Route.SerializeToString,
                response_deserializer=srv6__route__pb2.RouteReply.FromString,
                )
        self.ReplaceRoute = channel.unary_unary(
                '/Seg6Service/ReplaceRoute',
                request_serializer=srv6__route__pb2.Route.SerializeToString,
                response_deserializer=srv6__route__pb2.RouteReply.FromString,
                )
        self.RemoveRoute = channel.unary_unary(
                '/Seg6Service/RemoveRoute',
                request_serializer=srv6__route__pb2.Route.SerializeToString,
                response_deserializer=srv6__route__pb2.RouteReply.FromString,
                )
        self.GetRoutes = channel.unary_unary(
                '/Seg6Service/GetRoutes',
                request_serializer=srv6__route__pb2.GetRoutesRequest.SerializeToString,
                response_deserializer=srv6__route__pb2.GetRoutesReply.FromString,
                )


class Seg6ServiceServicer(object):
    """*
    Route Service on Agent
    """

    def AddRoute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaceRoute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveRoute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoutes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Seg6ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.AddRoute,
                    request_deserializer=srv6__route__pb2.Route.FromString,
                    response_serializer=srv6__route__pb2.RouteReply.SerializeToString,
            ),
            'ReplaceRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaceRoute,
                    request_deserializer=srv6__route__pb2.Route.FromString,
                    response_serializer=srv6__route__pb2.RouteReply.SerializeToString,
            ),
            'RemoveRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveRoute,
                    request_deserializer=srv6__route__pb2.Route.FromString,
                    response_serializer=srv6__route__pb2.RouteReply.SerializeToString,
            ),
            'GetRoutes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoutes,
                    request_deserializer=srv6__route__pb2.GetRoutesRequest.FromString,
                    response_serializer=srv6__route__pb2.GetRoutesReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Seg6Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Seg6Service(object):
    """*
    Route Service on Agent
    """

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
            srv6__route__pb2.Route.SerializeToString,
            srv6__route__pb2.RouteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplaceRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Seg6Service/ReplaceRoute',
            srv6__route__pb2.Route.SerializeToString,
            srv6__route__pb2.RouteReply.FromString,
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
            srv6__route__pb2.Route.SerializeToString,
            srv6__route__pb2.RouteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoutes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Seg6Service/GetRoutes',
            srv6__route__pb2.GetRoutesRequest.SerializeToString,
            srv6__route__pb2.GetRoutesReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
