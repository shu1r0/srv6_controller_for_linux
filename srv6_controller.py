from logging import INFO, getLogger

from srv6_grpc.srv6_client import SRv6Client
from utils.log import get_stream_handler, get_file_handler


class SRv6Node(SRv6Client):

    def __init__(self, name, ip, port):
        super(SRv6Node, self).__init__(ip, port)
        self.name = name


class SRv6Controller:

    def __init__(self, yml_file=None, log_level=INFO, log_file=None):
        self.nodes = []
        self._yml_file = yml_file

        self.logger = getLogger(__name__)
        self.logger.setLevel(log_level)
        self.logger.addHandler(get_stream_handler(log_level))
        if log_file:
            self.logger.addHandler(get_file_handler(log_file, log_level))

    def register_node(self, name, ip, port):
        node = SRv6Node(name, ip, port)
        self.nodes.append(node)

    def get(self, name):
        for n in self.nodes:
            if name == n.name:
                return n
        raise KeyError

    def connect(self, name):
        self.logger.info("gRPC client connect to server(ip={}, port={})".format(self.get(name).ip, self.get(name).port))
        self.get(name).establish_channel()

    def add_route(self, name, destination, segments, seg6_mode, dev):
        self.get(name).add_route(destination, segments, seg6_mode, dev)

    def remove_route(self, name, destination, segments, seg6_mode, dev):
        self.get(name).remove_route(destination, segments, seg6_mode, dev)

    def read_yml(self, yml_file=None):
        if yml_file is None:
            yml_file = self._yml_file
        pass


if __name__ == '__main__':
    controller = SRv6Controller()
    controller.register_node('R1', '127.0.0.1', '8889')
    controller.connect('R1')