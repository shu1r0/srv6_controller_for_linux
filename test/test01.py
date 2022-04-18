from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

from net import SRv6Net


def setup():
    net = SRv6Net()

    c1 = net.addHost('c1', ip=None, inNamespace=True)

    for i in range(1, 7):
        net.addRouter("r{}".format(i), inNamespace=True)
        net.addLink("r{}".format(i), "c1",
                    intfName1="r{}_c1".format(i), params1={"ip": "192.168.10{}.1/24".format(i)},
                    intfName2="c1_r{}".format(i), params2={"ip": "192.168.10{}.2/24".format(i)})

    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')

    net.addLink("r1", h1,
                intfName1="r1_h1", params1={"ip": "192.168.0.1/24"},
                intfName2="h1_r1", params2={"ip": "192.168.0.2/24"})
    net.addLink("r6", h2,
                intfName1="r6_h2", params1={"ip": "192.168.1.1/24"},
                intfName2="h2_r6", params2={"ip": "192.168.1.2/24"})
    net.addLink("r6", h3,
                intfName1="r6_h3", params1={"ip": "192.168.2.1/24"},
                intfName2="h3_r6", params2={"ip": "192.168.2.2/24"})

    net.addLink("r1", "r2", intfName1="r1_r2", intfName2="r2_r1")
    net.addLink("r1", "r3", intfName1="r1_r3", intfName2="r3_r1")

    net.addLink("r2", "r4", intfName1="r2_r4", intfName2="r4_r2")
    net.addLink("r2", "r3", intfName1="r2_r3", intfName2="r3_r2")

    net.addLink("r3", "r5", intfName1="r3_r5", intfName2="r5_r3")

    net.addLink("r4", "r6", intfName1="r4_r6", intfName2="r6_r4")
    net.addLink("r4", "r5", intfName1="r4_r5", intfName2="r5_r4")

    net.addLink("r5", "r6", intfName1="r5_r6", intfName2="r6_r5")

    net.start()

    net.get("h1").cmd("ip -6 addr add fc00:1::1/64 dev h1_r1")
    net.get("h1").cmd("ip -6 route add default dev h1_r1 via fc00:1::2")
    net.get("r1").address6add("fc00:1::2/64", "r1_h1")

    net.get("r1").address6add("fc00:a::1/64", "r1_r2")
    net.get("r2").address6add("fc00:a::2/64", "r2_r1")

    net.get("r1").address6add("fc00:b::1/64", "r1_r3")
    net.get("r3").address6add("fc00:b::2/64", "r3_r1")

    net.get("r2").address6add("fc00:c::1/64", "r2_r3")
    net.get("r3").address6add("fc00:c::2/64", "r3_r2")

    net.get("r2").address6add("fc00:d::1/64", "r2_r4")
    net.get("r4").address6add("fc00:d::2/64", "r4_r2")

    net.get("r3").address6add("fc00:e::1/64", "r3_r5")
    net.get("r5").address6add("fc00:e::2/64", "r5_r3")

    net.get("r4").address6add("fc00:f::1/64", "r4_r5")
    net.get("r5").address6add("fc00:f::2/64", "r5_r4")

    net.get("r4").address6add("fc00:aa::1/64", "r4_r6")
    net.get("r6").address6add("fc00:aa::2/64", "r6_r4")

    net.get("r5").address6add("fc00:ab::1/64", "r5_r6")
    net.get("r6").address6add("fc00:ab::2/64", "r6_r5")

    net.get("h2").cmd("ip -6 addr add fc00:2::1/64 dev h2_r6")
    net.get("h2").cmd("ip -6 route add default dev h2_r6 via fc00:2::2")
    net.get("r6").address6add("fc00:2::2/64", "r6_h2")
    
    net.get("h3").cmd("ip -6 addr add fc00:3::1/64 dev h3_r6")
    net.get("h3").cmd("ip -6 route add default dev h3_r6 via fc00:3::2")
    net.get("r6").address6add("fc00:3::2/64", "r6_h3")
    
    net.get("r1").start_srv6_agent()
    net.get("r6").start_srv6_agent()

    CLI(net)

    net.stop()

if __name__ == "__main__":
    setup()
