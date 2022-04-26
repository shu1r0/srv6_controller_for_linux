from logging import INFO, DEBUG, getLogger
import argparse
import yaml
import time

from srv6_grpc.srv6_client import SRv6Client
from utils.log import get_stream_handler, get_file_handler


class SRv6Node(SRv6Client):
    """SRv6 Node

    Attributes:
        name (string) : node name
    """

    def __init__(self, name, ip, port, logger=None):
        if logger is None:
            logger = getLogger(__name__)
        super(SRv6Node, self).__init__(ip, port, logger)
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Node name={} ip={} port={}>".format(self.name, self.ip, self.port)


class SRv6ControllerBase:
    """SRv6 Controller"""

    def __init__(self, logger=None):
        self.nodes: list[SRv6Node] = []
        self.logger = logger

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
        self.nodes.append(node)
        return node

    def get(self, node):
        """get SRv6 Node

        Args:
            node (str or SRv6Node) : node name

        Returns:
            SRv6Node
        """
        if isinstance(node, SRv6Node):
            return node
        if isinstance(node, str):
            for n in self.nodes:
                if node == n.name:
                    return n
        raise KeyError

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
        """
        connect all node
        """
        for node in self.nodes:
            if not self.is_connected(node.name):
                self.connect(node.name)

    def close_all(self):
        for node in self.nodes:
            node.close_channel()

    def add_route(self, name, destination, gateway=None, dev=None, metric=None, table=None, encap=None):
        self.get(name).add_route(destination, gateway, dev, metric, table, encap)

    def remove_route(self, name, destination, gateway=None, dev=None, metric=None, table=None, encap=None):
        self.get(name).remove_route(destination, gateway, dev, metric, table, encap)

    def start(self):
        pass

    def stop(self):
        self.close_all()


class SRv6Controller(SRv6ControllerBase):
    """SRv6 Controller"""

    def __init__(self, yml_file=None, logger=None):
        super(SRv6Controller, self).__init__(logger=logger)
        self._route_conf: list = []
        if yml_file is not None:
            self.read_yml(yml_file)

        self.logger = logger if logger else getLogger(__name__)

    def read_yml(self, yml_file):
        with open(yml_file) as f:
            dct = yaml.safe_load(f)
            nodes = dct.get('nodes')
            for node in nodes:
                name = node.get('name')
                ip = node.get('ip', "127.0.0.1")
                port = node.get('port')
                # get routes
                routes = node.get('route', [])
                # get headend behavior
                headend_routes = node.get('headend', [])
                # get end behavior
                end_routes = node.get('end', [])

                self.add_node(name, ip, port)

                for route in routes:
                    route['name'] = name
                    self._route_conf.append(route)
                # headend behavior
                for route in headend_routes:
                    route['name'] = name
                    headend = {
                        'type': 'seg6',
                        'mode': route.pop('mode', None),
                        'segments': route.pop('segments', None)
                    }
                    # ip command's encap route
                    route['encap'] = headend
                    self._route_conf.append(route)
                # end behavior
                for route in end_routes:
                    route['name'] = name
                    end = {
                        'type': 'seg6local',
                        'action': route.pop('action', None),
                        'nh4': route.pop('nh4', None),
                        'nh6': route.pop('nh6', None),
                        'srh': route.pop('srh', None)
                    }
                    if end.get('srh'):
                        end['srh'] = {
                            'segments': end['srh'].get('segment'),
                            'hmac': end['srh'].get('hmac')
                        }
                    # ip encap route
                    route['encap'] = end
                    self._route_conf.append(route)

    def add_routes(self):
        for route in self._route_conf:
            self.add_route(**route)

    def start(self):
        self.logger.info("start controller (nodes = {})".format(self.nodes))
        self.connect_all()
        self.add_routes()


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

    controller = SRv6Controller(yml_file=yml_file, logger=logger)
    controller.start()
