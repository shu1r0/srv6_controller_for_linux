from pyroute2 import IPRoute

from srv6_route_pb2 import *
import srv6_route_pb2_grpc


class SRv6Service(srv6_route_pb2_grpc.Seg6ServiceServicer):
    """gRPC SRv6 Service

    Attributes:
        ip (IPRoute) : netlink socket
        logger (Logger) : logger
    """

    def __init__(self, logger):
        # get access to the netlink socket
        self.ip = IPRoute()
        self.logger = logger

    def AddRoute(self, request, context):
        self.logger.debug("AddRoute called by peer({})".format(context.peer()))
        params = self._route_req_2_params(request)
        if params:
            self._add_route(**params)
            return Seg6RouteReply(status=0)
        else:
            return Seg6RouteReply(status=-1)

    def RemoveRoute(self, request, context):
        self.logger.debug("RemoveRoute called by peer({})".format(context.peer()))
        params = self._route_req_2_params(request)
        if params:
            self._del_route(**params)
            return Seg6RouteReply(status=0)
        else:
            return Seg6RouteReply(status=-1)

    def ShowRoute(self, request, context):
        self.logger.debug("ShowRoute called by peer({})".format(context.peer()))
        routes = self.ip.get_routes()
        raise NotImplementedError

    def _route_req_2_params(self, route_req):
        links = self.ip.link_lookup(ifname=route_req.dev)
        if len(links) == 0:
            return None
        idx = links[0]
        mode_value = route_req.seg6Mode
        mode_name = Seg6Mode.Name(mode_value).lower()
        segments = [segment.segment for segment in route_req.segments]
        return {'dst': route_req.destination, 'idx': idx, 'encap_mode': mode_name, 'encap_segs': segments}

    def _add_route(self, dst, idx, encap_mode, encap_segs):
        """add seg6 route

        https://github.com/svinota/pyroute2/blob/5ce9ccae0e47e02873f8d12d9e18ed4734e805fc/pyroute2.core/pr2modules/iproute/linux.py#L1787

        Args:
            dst (str) : destination
            idx (int) : out going traffic interface index
            encap_mode (str) : seg6 encap mode (e.g. 'encap')
            encap_segs (list[str]) : segments
        """
        self.ip.route('add',
                      dst=dst,
                      oif=idx,
                      encap={'type': 'seg6',
                             'mode': encap_mode,
                             'segs': encap_segs})

    def _del_route(self, dst, idx, encap_mode, encap_segs):
        """delete seg6 route

        https://github.com/svinota/pyroute2/blob/5ce9ccae0e47e02873f8d12d9e18ed4734e805fc/pyroute2.core/pr2modules/iproute/linux.py#L1787

        Args:
            dst (str) : destination
            idx (int) : out going traffic interface index
            encap_mode (str) : seg6 encap mode (e.g. 'encap')
            encap_segs (list[str]) : segments
        """
        self.ip.route('del',
                      dst=dst,
                      oif=idx,
                      encap={'type': 'seg6',
                             'mode': encap_mode,
                             'segs': encap_segs})



