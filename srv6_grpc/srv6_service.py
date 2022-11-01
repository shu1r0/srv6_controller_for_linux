from pyroute2 import IPRoute

from srv6_route_pb2 import Route, RouteReply, ReplyRoute, Seg6Mode, Seg6Type, Seg6LocalAction, GetRoutesReply
import srv6_route_pb2_grpc


Seg6LocalAction2string = {
    Seg6LocalAction.END: "End",
    Seg6LocalAction.END_X: "End.X",
    Seg6LocalAction.END_T: "End.T",
    Seg6LocalAction.END_DX2: "End.DX2",
    Seg6LocalAction.END_DX6: "End.DX6",
    Seg6LocalAction.END_DX4: "End.DX4",
    Seg6LocalAction.END_DT6: "End.DT6",
    Seg6LocalAction.END_DT4: "End.DT4",
    Seg6LocalAction.END_B6: "End.B6",
    Seg6LocalAction.END_B6_ENCAP: "End.B6.ENCAP",
    Seg6LocalAction.END_BM: "End.BM",
    Seg6LocalAction.END_S: "End.S",
    Seg6LocalAction.END_AS: "End.AS",
    Seg6LocalAction.END_AM: "End.AM",
    Seg6LocalAction.END_BPF: "End.BPF",
    Seg6LocalAction.END_DT46: "End.DT46",
}


class SRv6Service(srv6_route_pb2_grpc.Seg6ServiceServicer):
    """gRPC SRv6 Service

    Attributes:
        ipr (IPRoute) : netlink socket
        logger (Logger) : logger
    """

    def __init__(self, logger):
        # get access to the netlink socket
        self.ipr = IPRoute()
        self.logger = logger

    def __del__(self):
        self.ipr.close()

    def AddRoute(self, request, context):
        self.logger.debug("AddRoute called by peer({})".format(context.peer()))
        params = self._route_req_2_params(request)
        try:
            self._add_route(**params)
            return RouteReply(status=0)
        except Exception:
            return RouteReply(status=-1)

    def RemoveRoute(self, request, context):
        self.logger.debug("RemoveRoute called by peer({})".format(context.peer()))
        params = self._route_req_2_params(request)
        try:
            self._del_route(**params)
            return RouteReply(status=0)
        except Exception:
            return RouteReply(status=-1)

    def GetRoutes(self, request, context):
        self.logger.debug("GetRoutes called by peer({})".format(context.peer()))
        routes = self.ipr.get_routes()
        raise NotImplementedError

    def _route_req_2_params(self, route_req: Route):
        # route parameter
        params = {
            "dst": route_req.destination
        }
        # gateway
        if route_req.gateway:
            params["gateway"] = route_req.gateway
        # get link
        links = self.ipr.link_lookup(ifname=route_req.dev) if route_req.dev else []
        if len(links) > 0:
            params["oif"] = links[0]

        # metric and table
        if route_req.metric:
            params["metric"] = route_req.metric
        if route_req.table:
            params["table"] = route_req.table

        # encap parameter
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
            # parameters
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
            if route_req.seg6local_encap.WhichOneof("param") == "oif":
                links = self.ipr.link_lookup(ifname=route_req.seg6local_encap.oif) if route_req.seg6local_encap.oif else []
                if len(links) > 0:
                    encap_params["oif"] = links[0]
            if route_req.seg6local_encap.WhichOneof("param") == "table":
                encap_params["vrf_table"] = route_req.seg6local_encap.table
            params["encap"] = encap_params

        return params

    def _add_route(self, dst, **params):
        """add seg6 route

        References:
            https://github.com/svinota/pyroute2/blob/5ce9ccae0e47e02873f8d12d9e18ed4734e805fc/pyroute2.core/pr2modules/iproute/linux.py#L1787

        Args:
            dst (str) : destination
            idx (int) : out going traffic interface index
            encap_mode (str) : seg6 encap mode (e.g. 'encap')
            encap_segs (list[str]) : segments
        """
        # self.logger.debug("add route dst={}, {}".format(dst, params))
        try:        
            self.ipr.route('add', dst=dst, **params)
            self.logger.debug("add route dst={}, {}".format(dst, params))
        except Exception as e:
            self.logger.error(e)
            raise e

    def _del_route(self, dst, **params):
        """delete seg6 route

        References:
            https://github.com/svinota/pyroute2/blob/5ce9ccae0e47e02873f8d12d9e18ed4734e805fc/pyroute2.core/pr2modules/iproute/linux.py#L1787

        Args:
            dst (str) : destination
            idx (int) : out going traffic interface index
            encap_mode (str) : seg6 encap mode (e.g. 'encap')
            encap_segs (list[str]) : segments (e.g. ['2000::5', '2000::6'])
        """
        self.logger.debug("delete route dst={}, {}".format(dst, params))
        try:
            self.ipr.route('del', dst=dst, **params)
        except Exception as e:
            self.logger.error(e)
            raise e
    
    def _get_routes(self):
        """get route

        References:
            https://github.com/svinota/pyroute2/blob/4e9e7d50596e6375ff0d19aaf572dd3c8f53c2db/pyroute2.core/pr2modules/iproute/linux.py#L395
            https://github.com/svinota/pyroute2/blob/4e9e7d50596e6375ff0d19aaf572dd3c8f53c2db/pyroute2.core/pr2modules/iproute/linux.py#L1705

        Notes:
            ipr.get_routes() is a hack. The detail is https://docs.pyroute2.org/iproute.html#pyroute2.iproute.linux.RTNL_API.get_routes

        Returns:
            Routes
        """
        routes = self.ipr.get_routes()
        return routes

    def _parse_routes(self, routes):
        pass
    
    def _parse_routes(self, routes: list):
        """

        Args:
            route:

        Returns:
            ReplyRoute

        Todo:
            * parse route
        """
        rep = GetRoutesReply()
        for r in routes:
            pass

    def _parse_route(self, route: dict) -> ReplyRoute:
        rep_route = ReplyRoute()
        rep_route.dst = route.get("dst")
        rep_route.oif = route.get("oif")
        rep_route.gateway = route.get("gateway", None)
        rep_route.priority = route.get("priority", None)
        pass
