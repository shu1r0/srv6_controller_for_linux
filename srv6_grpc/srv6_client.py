import grpc

import srv6_route_pb2_grpc
from srv6_route_pb2 import *


class ChangeRouteException(Exception):
    pass


class NoChannelException(Exception):
    pass


class SRv6Client:
    """SRv6 Client

    Attributes:
        ip (string) : target ip address
        port (string) : target port number
        channel : grpc channel
        stub : grpc service stub
    """

    def __init__(self, ip, port, logger):
        self.ip = ip
        self.port = port if isinstance(port, str) else str(port)
        self.channel = None
        self.stub = None
        self.logger = logger

    def establish_channel(self):
        """establish grpc channel"""
        self.channel = grpc.insecure_channel(self.ip + ':' + self.port, options=(('grpc.enable_http_proxy', 0),))
        self.stub = srv6_route_pb2_grpc.Seg6ServiceStub(self.channel)

    def close_channel(self):
        if self.channel:
            self.channel.close()

    def has_established_channel(self):
        """The client has established grpc channel"""
        return self.channel is not None and self.stub is not None

    def add_route(self, destination, gateway=None, dev=None, metric=None, table=None, encap=None):
        """add srv6 route"""
        if not self.has_established_channel():
            raise NoChannelException
        route_req = self._params_2_route_req(destination, gateway, dev, metric, table, encap)
        print(route_req)
        reply = self.stub.AddRoute(route_req)
        if reply.status != 0:
            raise ChangeRouteException
        return self

    def remove_route(self, destination, gateway=None, dev=None, metric=None, table=None, encap=None):
        """remove srv6 route"""
        if not self.has_established_channel():
            raise NoChannelException
        route_req = self._params_2_route_req(destination, gateway, dev, metric, table, encap)
        reply = self.stub.RemoveRoute(route_req)
        if reply.status != 0:
            raise ChangeRouteException
        return self

    def show_routes6(self):
        raise NotImplementedError

    def _params_2_route_req(self, destination, gateway=None, dev=None, metric=None, table=None, encap=None):
        route_req = Route()
        route_req.destination = destination
        if gateway:
            route_req.gateway = gateway
        if dev:
            route_req.dev = dev
        if metric:
            route_req.metric = metric
        if table:
            route_req.table = table
        if encap:
            type = encap.pop("type", None)
            if type and type == "seg6":
                seg6_encap = Seg6Encap()
                seg6_encap.type = Seg6Type.SEG6
                
                if encap.pop("mode", None) == "encap":
                    seg6_encap.mode = Seg6Mode.ENCAP
                segments = encap.pop("segments", [])
                for segment in segments:
                    seg6_encap.segments.append(segment)
                route_req.seg6_encap.CopyFrom(seg6_encap)
            elif type and type == "seg6local":
                seg6local_encap = Seg6LocalEncap()
                seg6local_encap.type = Seg6Type.SEG6LOCAL
                action = encap.pop("action", "")
                action = '_'.join(action.split(".")).upper()
                seg6local_encap.action = Seg6LocalAction.Value(action)
                nh6 = e
                ncap.pop("nh6", None)
                if nh6:
                    seg6local_encap.nh6 = nh6
                nh4 = encap.pop("nh4", None)
                if nh6:
                    seg6local_encap.nh4 = nh4
                srh = encap.pop("srh", None)
                if srh:
                    segments = srh.pop("segments", [])
                    for segment in segments:
                        seg6local_encap.srh.segments.append(segment)
                    hmac = srh.pop("hmac", None)
                    if hmac:
                        seg6local_encap.srh.hmac = hmac
                route_req.seg6_encap.CopyFrom(seg6local_encap)
        return route_req
