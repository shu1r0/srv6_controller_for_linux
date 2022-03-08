# coding: utf-8

# python3 srv6_controller.py --config test/test1.yaml
# sudo python3 srv6_agent.py --ip 0.0.0.0 --port 30000


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

from functools import partial

def setup():
    net = Mininet()

    r1 = net.addHost('r1', inNamespace=True)
    r2 = net.addHost('r2', inNamespace=True)
    c1 = net.addHost('c1', inNamespace=True)
    h1 = net.addHost('h1', ip="192.168.0.1/24")
    h2 = net.addHost('h2', ip="192.168.1.1/24")

    net.addLink(r1, h1, intfName1="r1_h1", intfName2="h1_eth0")
    net.addLink(r2, h2, intfName1="r2_h2", intfName2="h2_eth0")
    net.addLink(r1, r2, intfName1="r1_r2", intfName2="r2_r1")

    net.addLink(r1, c1, intfName1="r1_c1", intfName2="c1_r1")
    net.addLink(r2, c1, intfName1="r2_c1", intfName2="c1_r2")

    net.start()

    # r1 address config
    r1.cmd("sysctl -w net.ipv6.conf.all.forwarding=1")
    r1.cmd("sysctl -w net.ipv6.conf.all.seg6_enabled=1")
    r1.cmd("sysctl -w net.ipv6.conf.all.seg6_require_hmac=0")
    r1.cmd("ip -6 addr add a::1/64 dev r1_r2")
    r1.cmd("ip addr add 192.168.0.254/24 dev r1_h1")
    r1.cmd("ip addr add 192.168.11.1/24 dev r1_c1")
    r1.cmd("cd ..; python3 srv6_agent.py -v --ip 0.0.0.0 --port 30000 --log_file test1_r1.log &")

    # r2 address config
    r2.cmd("sysctl -w net.ipv6.conf.all.forwarding=1")
    r2.cmd("sysctl -w net.ipv6.conf.all.seg6_enabled=1")
    r2.cmd("sysctl -w net.ipv6.conf.all.seg6_require_hmac=0")
    r2.cmd("ip -6 addr add a::2/64 dev r2_r1")
    r2.cmd("ip addr add 192.168.1.254/24 dev r2_h2")
    r2.cmd("ip addr add 192.168.22.1/24 dev r2_c1")
    r2.cmd("cd ..; python3 srv6_agent.py -v --ip 0.0.0.0 --port 30000 --log_file test1_r2.log &")

    # c1 address config
    c1.cmd("ip addr add 192.168.11.2/24 dev c1_r1")
    c1.cmd("ip addr add 192.168.22.2/24 dev c1_r2")

    # host address config
    h1.cmd("ip route add default via 192.168.0.254")
    h2.cmd("ip route add default via 192.168.1.254")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    setup()

