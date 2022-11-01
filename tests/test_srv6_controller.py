from time import sleep
from unittest import TestCase, main

import yaml

from srv6_agent import SRv6Agent
from srv6_controller import SRv6Controller

local_conf1 = """\
nodes:
  - name: localhost
    ip: 127.0.0.1
    port: 30000
    route:
      - destination: "192.168.254.0/24"
        table: 100
        dev: eth0
      - destination: "192.168.253.0/24"
        table: 100
        dev: eth0
"""


class TestSRv6Controller(TestCase):

    def setUp(self) -> None:
        self.agent = SRv6Agent(ip="[::]", port=30000)

        def add_route(**param):
            self.add_route_param = param

        def del_route(**param):
            self.del_route_param = param

        # set stub
        self.agent.service._add_route = add_route
        self.agent.service._del_route = del_route

    def test_send(self):
        self.agent.start(block=False)

        self.controller = SRv6Controller()
        self.controller.read_conf(yaml.safe_load(local_conf1))
        self.controller.start()
        sleep(1)
        print(self.add_route_param)
