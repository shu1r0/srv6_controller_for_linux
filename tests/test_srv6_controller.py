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
        dev: lo
      - destination: "192.168.253.0/24"
        table: 100
        dev: lo
    end:
      - destination: "fdbb:c1::2:0"
        action: End.BPF
        bpf:
          fd: 1
          name: "End.TEST"
        dev: lo
"""


class TestSRv6Controller(TestCase):

    def setUp(self) -> None:
        self.agent = SRv6Agent(ip="[::]", port=30000)

        self.add_route_param = []
        self.replace_route_param = []
        self.del_route_param = []

        def add_route(**param):
            self.add_route_param.append(param)

        def replace_route(**param):
            self.replace_route_param.append(param)

        def del_route(**param):
            self.del_route_param.append(param)

        # set stub
        self.agent.service._add_route = add_route
        self.agent.service._del_route = del_route
        self.agent.service._replace_route = replace_route

    def test_send(self):
        self.agent.start(block=False)

        self.controller = SRv6Controller()
        self.controller.read_conf(yaml.safe_load(local_conf1))
        self.controller.start()
        sleep(1)
        # print(self.add_route_param)
        print(self.replace_route_param)
