from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info

controller_ip_base = "10.10."
controller_ip_count = 1


daemons = """
zebra=yes
bgpd=yes

vtysh_enable=yes
zebra_options=" -s 90000000 --daemon -A 127.0.0.1"
bgpd_options="   --daemon -A 127.0.0.1"
"""

vtysh = """
hostname {name}
service integrated-vtysh-config
"""


class SRv6Controller(Node):

    def __init__(self, name, ip=None, **params):
        super().__init__(name, inNamespace=False, ip=ip, **params)


class SRv6Node(Node):

    def __init__(self, name, **params):
        super().__init__(name, **params)

    def config(self, **params):
        self.cmd("ifconfig lo up")
        self.cmd("sysctl -w net.ipv4.ip_forward=1")
        self.cmd("sysctl -w net.ipv6.conf.all.forwarding=1")
        self.cmd("sysctl -w net.ipv6.conf.all.seg6_enabled=1")
        self.cmd("sysctl -w net.ipv6.conf.all.seg6_require_hmac=0")

        for i in self.nameToIntf.keys():
            self.cmd("sysctl -w net.ipv6.conf.{}.seg6_enabled=1".format(i))


class FRR(SRv6Node):
    """FRR Node"""

    PrivateDirs = ["/etc/frr", "/var/run/frr"]

    def __init__(self, name, inNamespace=True, **params):
        params.setdefault("privateDirs", [])
        params["privateDirs"].extend(self.PrivateDirs)
        super().__init__(name, inNamespace=inNamespace, **params)
        
    def config(self, **params):
        super().config(**params)
        self.start_frr_service()

    def start_frr_service(self):
        """start FRR"""
        self.set_conf("/etc/frr/daemons", daemons)
        self.set_conf("/etc/frr/vtysh.conf", vtysh.format(name=self.name))
        print(self.cmd("/usr/lib/frr/frrinit.sh start"))

    def set_conf(self, file, conf):
        """set frr config"""
        self.cmd("""\
cat << 'EOF' | tee {}
{}
EOF""".format(file, conf))

    def vtysh_cmd(self, cmd=""):
        """exec vtysh commands"""
        cmds = cmd.split("\n")
        vtysh_cmd = "vtysh"
        for c in cmds:
            vtysh_cmd += " -c \"{}\"".format(c)
        return self.cmd(vtysh_cmd)


class SRv6Net(Mininet):

    def __init__(self, **params):
        super().__init__(**params)
        self.frr_routers = []
        self.srv6_controller = self._addSRv6Controller()

    def addSRv6Node(self, name, cls=SRv6Node, **params):
        """add SRv6Node"""
        global controller_ip_count
        r = self.addHost(name=name, cls=cls, **params)
        self.addLink(name, self.srv6_controller,
                     intfName1="{}_c1".format(name), params1={"ip": controller_ip_base + "{}.1/24".format(controller_ip_count)},
                     intfName2="c1_{}".format(name), params2={"ip": controller_ip_base + "{}.2/24".format(controller_ip_count)})
        controller_ip_count += 1
        return r
    
    def start_agents(self, agent_path):
        """start srv6 agent"""
        info('*** Start SRv6 agent:\n')
        for n in self.nameToNode.values():
            if isinstance(n, SRv6Node):
                # self.addLink(n)
                n.start_srv6_agent(agent_path)
                info(n.name + " " + n.IP() + "\n")


