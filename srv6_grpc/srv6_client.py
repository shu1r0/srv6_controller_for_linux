import grpc

import srv6_route_pb2_grpc
from srv6_route_pb2 import *


class ChangeRouteException(Exception):
    pass


class NoChannelException(Exception):
    pass


class SRv6Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.channel = None
        self.stub = None

    def establish_channel(self):
        self.channel = grpc.insecure_channel(self.ip + ':' + self.port)
        self.stub = srv6_route_pb2_grpc.Seg6ServiceStub(self.channel)

    def has_established_channel(self):
        return self.channel is not None and self.stub is not None

    def add_route(self, destination, segments, seg6_mode, dev):
        if not self.has_established_channel():
            raise NoChannelException
        route_req = self._params_2_route_req(destination, segments, seg6_mode, dev)
        reply = self.stub.AddRoute(route_req)
        if reply.status != 0:
            raise ChangeRouteException

    def remove_route(self, destination, segments, seg6_mode, dev):
        if not self.has_established_channel():
            raise NoChannelException
        route_req = self._params_2_route_req(destination, segments, seg6_mode, dev)
        reply = self.stub.RemoveRoute(route_req)
        if reply.status != 0:
            raise ChangeRouteException

    def show_routes6(self):
        raise NotImplementedError

    def _params_2_route_req(self, destination, segments, seg6_mode, dev):
        route_req = Seg6RouteRequest()
        route_req.destination = destination
        for segment in segments:
            segment_req = route_req.segments.add()
            segment_req.segment = segment
        route_req.seg6Mode = Seg6Mode.Value(seg6_mode)
        route_req.dev = dev
        return route_req
