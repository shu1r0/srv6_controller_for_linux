from cmd import Cmd
from logging import INFO, DEBUG, getLogger
import argparse
import yaml

from srv6_grpc.srv6_client import SRv6Client
from utils.log import get_stream_handler, get_file_handler


class SRv6Node(SRv6Client):
    """SRv6 Node

    Attributes:
        name (string) : node name
    """

    def __init__(self, name: str, ip: str, port: str or int, logger=None):
        if logger is None:
            logger = getLogger(__name__)
        super(SRv6Node, self).__init__(ip, port, logger)
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, SRv6Node):
            return False
        if self.name == other.name:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<SRv6Node name={} ip={} port={}>".format(self.name, self.ip, self.port)


class SRv6Controller:
    """SRv6 Controller"""

    def __init__(self, logger=None):
        self.nodes: list[SRv6Node] = []
        self.logger = logger if logger else getLogger(__name__)
        
        self._route_conf: list = []
        self.default_method = "replace"

    @property
    def route_conf(self):
        return self._route_conf

    def add_node(self, name, ip, port):
        """add SRv6 Node

        Args:
            name (str) : node name
            ip (str) : node ip address
            port (str or int) : node port number

        Returns:
            SRv6Node
        """
        node = SRv6Node(name, ip, port, logger=self.logger)
        if node not in self.nodes:
            self.nodes.append(node)
        return node

    def get(self, node):
        """get SRv6 Node

        Args:
            node (str) : node name

        Returns:
            SRv6Node
        """
        if isinstance(node, SRv6Node):
            return node
        if isinstance(node, str):
            for n in self.nodes:
                if node == n.name:
                    return n
        raise KeyError("{} SRv6 node not found".format(node))

    def connect(self, name):
        """connect to node

        Args:
            name (str) :
        """
        self.logger.info("gRPC client connect to server(ip={}, port={})".format(self.get(name).ip, self.get(name).port))
        node = self.get(name)
        node.establish_channel()

    def is_connected(self, name):
        """Is connected to the node

        Args:
            name (str) :

        Returns:
            bool
        """
        return self.get(name).has_established_channel()

    def connect_all(self):
        """connect all node
        """
        for node in self.nodes:
            if not self.is_connected(node.name):
                self.connect(node.name)

    def close_all(self):
        for node in self.nodes:
            node.close_channel()

    def add_route(self, name, destination, gateway=None, dev=None, metric=None, table=None, encap=None):
        try:
            return self.get(name).add_route(destination, gateway, dev, metric, table, encap)
        except Exception as e:
            self.logger.error("Add route error: {}".format(str(e)))

    def replace_route(self, name, destination, gateway=None, dev=None, metric=None, table=None, encap=None):
        try:
            return self.get(name).replace_route(destination, gateway, dev, metric, table, encap)
        except Exception as e:
            self.logger.error("Replace route error: {}".format(str(e)))

    def remove_route(self, name, destination, gateway=None, dev=None, metric=None, table=None, encap=None):
        try:
            return self.get(name).remove_route(destination, gateway, dev, metric, table, encap)
        except Exception as e:
            self.logger.error("Remove route error: {}".format(str(e)))

    def _run_conf_routes(self):
        """add read conf route"""
        for route in self._route_conf:
            method = route.pop("method", self.default_method)
            if method == "add":
                self.add_route(**route)
            elif method == "replace":
                self.replace_route(**route)
            elif method == "remove":
                self.remove_route(**route)
            else:
                self.logger.error("Invalid method {}".format(method))
        self._route_conf = []

    def start(self):
        self.logger.info("start controller (nodes = {})".format(self.nodes))
        self.connect_all()
        self._run_conf_routes()

    def stop(self):
        self.close_all()

    def read_yml(self, yml_file):
        """read yaml

        Args:
            yml_file (str) : yaml file path

        Returns:
            (list, list) : SRv6Node List and Route conf list
        """
        with open(yml_file) as f:
            dct = yaml.safe_load(f)
            return self.read_conf(dct)
    
    def read_conf(self, dct):
        added_nodes = []
        readed_routes = []
        # nodes
        nodes = dct.get('nodes')
        for node in nodes:
            name = node.get('name')
            ip = node.get('ip')
            port = node.get('port', None)
            if port is None:
                port = node.get("controller_port", None)
            # get routes
            routes = node.get('route', [])
            # get headend behavior
            headend_routes = node.get('headend', [])
            # get end behavior
            end_routes = node.get('end', [])
            added_node = self.add_node(name, ip, port)
            added_nodes.append(added_node)

            # routes
            for route in routes:
                # node name
                route['name'] = name
                route.setdefault("method", self.default_method)
                readed_routes.append(route)
            # headend behavior
            for route in headend_routes:
                # nodename
                route['name'] = name
                route.setdefault("method", self.default_method)
                headend = {
                    'type': 'seg6',
                    'mode': route.pop('mode', None),
                    'segments': route.pop('segments', None)
                }
                # ip command's encap route
                route['encap'] = headend
                readed_routes.append(route)
            # end behavior
            for route in end_routes:
                # node name
                route['name'] = name
                route.setdefault("method", self.default_method)
                end = {
                    'type': 'seg6local',
                    'action': route.pop('action', None),
                    'nh4': route.pop('nh4', None),
                    'nh6': route.pop('nh6', None),
                    'srh': route.pop('srh', None),
                    'oif': route.pop('oif', None),
                    'table': route.pop('table', None),
                    'bpf': route.pop('bpf', None),
                }
                if end.get('srh'):
                    end['srh'] = {
                        'segments': end['srh'].get('segment'),
                        'hmac': end['srh'].get('hmac')
                    }
                # ip encap route
                route['encap'] = end
                readed_routes.append(route)

        self._route_conf.extend(readed_routes)
        return added_nodes, readed_routes

    def reload_yml(self, yml_file):
        """clear cache and read yaml

        Args:
            yml_file:

        Returns:

        """
        self._route_conf = []
        return self.read_yml(yml_file)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--log_file', help="log file path")
    parser.add_argument('--config', help="config yml path")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    # print(args)
    log_level = DEBUG if args.verbose else INFO
    yml_file = args.config
    log_file = args.log_file

    logger = getLogger(__name__)
    logger.setLevel(log_level)
    logger.addHandler(get_stream_handler(log_level))
    if log_file:
        logger.addHandler(get_file_handler(log_file, log_level))

    controller = SRv6Controller(logger=logger)
    controller.read_yml(yml_file)
    controller.start()
