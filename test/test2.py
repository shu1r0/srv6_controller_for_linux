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
    r3 = net.addHost('r3', inNamespace=True)
    r4 = net.addHost('r4', inNamespace=True)

    c1 = net.addHost('c1', inNamespace=True)

    for r in [r1, r2, r3, r4]:
        intf1 = str(r) + "_c1"
        intf2 = "c1_" + str(r)
        net.addLink(r, c1, intfName1=intf1, intfName2=intf2)

    h1 = net.addHost('h1', ip="fc00:a::1/64")
    h2 = net.addHost('h2', ip="fc00:d::2/64")

    net.addLink(h1, r1, intfName1="h1_r1", intfName2="r1_h1")
    net.addLink(r1, r2, intfName1="r1_r2", intfName2="r2_r1")
    net.addLink(r2, r3, intfName1="r2_r3", intfName2="r3_r2")
    net.addLink(r2, r4, intfName1="r2_r4", intfName2="r4_r2")
    net.addLink(r3, h2, intfName1="r3_h2", intfName2="h2_r3")

    net.start()

    for node in [r1, r2, r3, r4, c1, h1, h2]:
        node.cmd("sysctl -w net.ipv6.conf.all.forwarding=1")
        node.cmd("sysctl -w net.ipv6.conf.all.seg6_enabled=1")

    # h1 config
    h1.cmd("ip addr add fc00:a::1/64 dev h1_r1")
    h1.cmd("ip -6 route add fc00:d::/64 via fc00:a::2")
    h1.cmd("ip -6 route add fc00:e::/64 via fc00:a::2")

    # r1 config
    r1.cmd("ip addr add fc00:a::2/64 dev r1_h1")
    r1.cmd("ip addr add fc00:b::1/64 dev r1_r2")

    r1.cmd("ip addr add 192.168.11.1/24 dev r1_c1")
    r1.cmd("cd ..; python3 srv6_agent.py -v --ip 0.0.0.0 --port 30000 --log_file test2_r1.log &")

    # r2 config
    r2.cmd("ip addr add fc00:b::2/64 dev r2_r1")
    r2.cmd("ip addr add fc00:c::1/64 dev r2_r3")
    r2.cmd("ip addr add fc00:e::1/64 dev r2_r4")

    r2.cmd("sysctl net.ipv6.conf.r2_r4.seg6_enabled=1")

    r2.cmd("ip addr add 192.168.22.1/24 dev r2_c1")
    r2.cmd("cd ..; python3 srv6_agent.py -v --ip 0.0.0.0 --port 30000 --log_file test2_r2.log &")

    # r3 config
    r3.cmd("ip addr add fc00:c::2/64 dev r3_r2")
    r3.cmd("ip addr add fc00:d::1/64 dev r3_h2")

    r3.cmd("sysctl net.ipv6.conf.r3_r2.seg6_enabled=1")

    r3.cmd("ip addr add 192.168.33.1/24 dev r3_c1")
    r3.cmd("cd ..; python3 srv6_agent.py -v --ip 0.0.0.0 --port 30000 --log_file test2_r3.log &")

    # r4 config
    r4.cmd("ip addr add fc00:e::2/64 dev r4_r2")

    r4.cmd("sysctl net.ipv6.conf.r4_r2.seg6_enabled=1")

    r4.cmd("ip addr add 192.168.44.1/24 dev r4_c1")
    r4.cmd("cd ..; python3 srv6_agent.py -v --ip 0.0.0.0 --port 30000 --log_file test2_r4.log &")

    # h2 config
    h2.cmd("ip addr add fc00:d::2/64 dev h2_r3")
    h2.cmd("ip -6 route add fc00:a::/64 via fc00:d::1")
    h2.cmd("sysctl net.ipv6.conf.h2_r3.seg6_enabled=1")

    # c1 address config
    c1.cmd("ip addr add 192.168.11.2/24 dev c1_r1")
    c1.cmd("ip addr add 192.168.22.2/24 dev c1_r2")
    c1.cmd("ip addr add 192.168.33.2/24 dev c1_r3")
    c1.cmd("ip addr add 192.168.44.2/24 dev c1_r4")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    setup()

