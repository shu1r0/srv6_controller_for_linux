from logging import getLogger, INFO
from concurrent import futures
import grpc

from srv6_grpc import srv6_route_pb2_grpc
from srv6_grpc.srv6_service import SRv6Service

from utils.log import get_file_handler, get_stream_handler


class SRv6Agent:
    """SRv6 Agent

    Attributes:
        service (SRv6Service) : gRPC SRv6 Service
        server (grpc.Server) : gRPC server
        ip (str) : server ip address
        port (str) : listening port
    """

    def __init__(self, ip, port, log_level=INFO, log_file=None):
        self.logger = getLogger(__name__)
        self.logger.setLevel(log_level)
        self.logger.addHandler(get_stream_handler(log_level))
        if log_file:
            self.logger.addHandler(get_file_handler(log_file, log_level))

        self.service = SRv6Service(logger=self.logger)
        self.server = None
        self.ip = ip
        self.port = port

    def start(self):
        """start server"""
        self.logger.info("server start (ip={}, port={})".format(self.ip, self.port))
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        srv6_route_pb2_grpc.add_Seg6ServiceServicer_to_server(
            self.service, self.server
        )
        self.server.add_insecure_port(self.ip + ':' + self.port)
        self.server.start()

    def stop(self):
        """stop server"""
        self.logger.info("server stop (ip={}, port={})".format(self.ip, self.port))
        self.server.stop(grace=None)


if __name__ == '__main__':
    agent = SRv6Agent(ip='127.0.0.1', port='50051')
    agent.start()
