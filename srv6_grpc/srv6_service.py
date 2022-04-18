from pyroute2 import IPRoute

from srv6_route_pb2 import Route, RouteReply, Seg6Mode, Seg6Type, Seg6LocalAction
import srv6_route_pb2_grpc


Seg6LocalAction2string = {
    Seg6LocalAction.END: "End",
    Seg6LocalAction.END_X: "End.X",
    Seg6LocalAction.END_DX4: "End.DX4",
    Seg6LocalAction.END_DX6: "End.DX6",
    Seg6LocalAction.END_B6: "End.B6",
    Seg6LocalAction.END_B6_ENCAPS: "End.B6.Encap"
}


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
            return RouteReply(status=0)
        else:
            return RouteReply(status=-1)

    def RemoveRoute(self, request, context):
        self.logger.debug("RemoveRoute called by peer({})".format(context.peer()))
        params = self._route_req_2_params(request)
        if params:
            self._del_route(**params)
            return RouteReply(status=0)
        else:
            return RouteReply(status=-1)

    def ShowRoute(self, request, context):
        self.logger.debug("ShowRoute called by peer({})".format(context.peer()))
        routes = self.ip.get_routes()
        raise NotImplementedError

    def _route_req_2_params(self, route_req: Route):
        params = {}
        params["dst"] = route_req.destination
        if route_req.gateway:
            params["gateway"] = route_req.gateway
        links = self.ip.link_lookup(ifname=route_req.dev) if route_req.dev else []
        if len(links) > 0:
            params["oif"] = links[0]
        if route_req.metric:
            params["metric"] = route_req.metric
        if route_req.table:
            params["table"] = route_req.table
        if route_req.WhichOneof("encap") == "seg6_encap":
            encap_params = {
                "type": Seg6Type.Name(route_req.seg6_encap.type).lower(),
                "mode": Seg6Mode.Name(route_req.seg6_encap.mode).lower(),
                "segs": route_req.seg6_encap.segments
            }
            params["encap"] = encap_params
        if route_req.WhichOneof("encap") == "seg6local_encap":
            encap_params = {
                "type": Seg6Type.Name(route_req.seg6local_encap.type).lower(),
                "action": Seg6LocalAction2string[route_req.seg6local_encap.action]
            }
            if route_req.seg6local_encap.WhichOneof("param") == "nh6":
                encap_params["nh6"] = route_req.seg6local_encap.nh6
            if route_req.seg6local_encap.WhichOneof("param") == "nh4":
                encap_params["nh4"] = route_req.seg6local_encap.nh4
            if route_req.seg6local_encap.WhichOneof("param") == "srh":
                srh_params = {
                    "segs": route_req.seg6local_encap.srh.segments
                }
                if route_req.seg6local_encap.srh.hmac:
                    srh_params["hmac"] = route_req.seg6local_encap.srh.hmac
                encap_params["srh"] = srh_params
            params["encap"] = encap_params
        return params

    def _add_route(self, dst, **params):
        """add seg6 route

        https://github.com/svinota/pyroute2/blob/5ce9ccae0e47e02873f8d12d9e18ed4734e805fc/pyroute2.core/pr2modules/iproute/linux.py#L1787

        Args:
            dst (str) : destination
            idx (int) : out going traffic interface index
            encap_mode (str) : seg6 encap mode (e.g. 'encap')
            encap_segs (list[str]) : segments
        """
        self.logger.debug("add route dst={}, {}".format(dst, params))
        try:        
            self.ip.route('add', dst=dst, **params)
        except Exception as e:
            self.logger.error(e)
            raise e

    def _del_route(self, dst, **params):
        """delete seg6 route

        https://github.com/svinota/pyroute2/blob/5ce9ccae0e47e02873f8d12d9e18ed4734e805fc/pyroute2.core/pr2modules/iproute/linux.py#L1787

        Args:
            dst (str) : destination
            idx (int) : out going traffic interface index
            encap_mode (str) : seg6 encap mode (e.g. 'encap')
            encap_segs (list[str]) : segments (e.g. ['2000::5', '2000::6'])
        """
        self.logger.debug("delete route dst={}, {}".format(dst, params))
        try:
            self.ip.route('del', dst=dst, **params)
        except Exception as e:
            self.logger.error(e)
            raise e

