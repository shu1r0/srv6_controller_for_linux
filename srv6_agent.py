from logging import getLogger, INFO, DEBUG
import argparse
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
        logger (Logger) : logger
    """

    def __init__(self, ip: str, port: str or int, log_level=INFO, log_file=None):
        # set logger
        self.logger = getLogger(__name__)
        self.logger.setLevel(log_level)
        self.logger.addHandler(get_stream_handler(log_level))
        if log_file:
            self.logger.addHandler(get_file_handler(log_file, log_level))

        self.service = SRv6Service(logger=self.logger)
        self.server = None
        self.ip = ip
        self.port = port if isinstance(port, int) else int(port)

    def __del__(self):
        self.stop()

    def start(self, block=True):
        """start server"""
        self.logger.info("server start (ip={}, port={})".format(self.ip, self.port))
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        srv6_route_pb2_grpc.add_Seg6ServiceServicer_to_server(
            self.service, self.server
        )
        self.server.add_insecure_port(self.ip + ':' + str(self.port))
        self.server.start()
        if block:
            self.server.wait_for_termination()

    def stop(self):
        """stop server"""
        self.logger.info("server stop (ip={}, port={})".format(self.ip, self.port))
        if self.server:
            self.server.stop(grace=None)


def get_args():
    """get args from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--log_file', help="log file path")

    parser.add_argument('--ip', help='server ip address', default="[::]")
    parser.add_argument('--port', help='listening port', default=30000)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    if args.verbose:
        log_level = DEBUG
    else:
        log_level = INFO
    log_file = args.log_file

    ip = args.ip
    port = args.port

    agent = SRv6Agent(ip=ip, port=port, log_level=log_level, log_file=log_file)
    try:
        agent.start()
    except KeyboardInterrupt:
        agent.stop()
