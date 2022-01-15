# coding: utf-8

# python3 srv6_controller.py --config test/test1.yaml


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

from functools import partial

def setup():
    net = Mininet()
    # ネットに繋がるようにする

    # net.addNAT().configDefault()
    #
    r1 = net.addHost('r1', inNamespace=True)
    r2 = net.addHost('r2', inNamespace=True)
    h1 = net.addHost('h1', ip="192.168.0.1/24")
    h2 = net.addHost('h2', ip="192.168.1.1/24")
    net.addLink(r1, h1, intfName1="r1_h1", intfName2="h1_eth0")
    net.addLink(r2, h2, intfName1="r2_h2", intfName2="h2_eth0")
    net.addLink(r1, r2, intfName1="r1_r2", intfName2="r2_r1")
    net.start()
    r1.cmd("ip -6 addr add a::1/64 dev r1_r2")
    r1.cmd("ip addr add 192.168.0.254/24 dev r1_h1")
    r1.cmd("ip -6 addr add a::2/64 dev r2_r1")
    r1.cmd("ip addr add 192.168.1.254/24 dev r2_h2")
    CLI(net)
    net.stop()

    # h1 = net.addHost('h1', inNamespace=True)
    # s1 = net.addSwitch("s1")
    # net.addNAT().configDefault()
    # net.addLink(h1, s1)
    # net.start()
    # CLI(net)
    # net.stop()



if __name__ == '__main__':
    setLogLevel('info')
    setup()

