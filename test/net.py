from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Node


class Router(Node):

    def __init__(self, name, **params):
        super().__init__(name, **params)

    def config(self, **params):
        super(Router, self).config(**params)
        self.cmd("sysctl -w net.ipv4.ip_forward=1")
        self.cmd("sysctl -w net.ipv6.conf.all.forwarding=1")
        self.cmd("sysctl -w net.ipv6.conf.all.seg6_enabled=1")
        self.cmd("sysctl -w net.ipv6.conf.all.seg6_require_hmac=0")

        for i in self.nameToIntf.keys():
            self.cmd("sysctl -w net.ipv6.conf.{}.seg6_enabled=1".format(i))

    def address6add(self, ipv6, intf_name):
        self.cmd("ip -6 addr add {} dev {}".format(ipv6, intf_name))

    def tcpdump(self, intf):
        cmd = "tcppdump -i " + intf + " -w " + intf + ".pcap &"
        return self.cmd(cmd)
    
    def start_srv6_agent(self):
        self.cmd("cd ..; python3 srv6_agent.py -v --ip 0.0.0.0 --port 30000 --log_file {}.log &".format(self.name))


class SRv6Net(Mininet):

    def __init__(self, **params):
        super().__init__(params)

    def addRouter(self, name, cls=Router, **params):
        """add FRR"""
        params["ip"] = None
        r = self.addHost(name=name, cls=cls, **params)
        return r


