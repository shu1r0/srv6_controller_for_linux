# vm name 
$name = "ubuntu-SRv6-dev"

# ------------------------------------------------------------
# Description
# ------------------------------------------------------------
$description = <<'EOS'

user: vagrant
password: vagrant
EOS


# ------------------------------------------------------------
# install basic package
# ------------------------------------------------------------
$install_package = <<SCRIPT
# install package
sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa

sudo apt-get -y update

sudo apt-get -y install build-essential
sudo apt-get -y install sshpass
sudo apt-get -y install python3
sudo apt-get -y install python3-pip

python3 -m pip install -U pip

sudo apt-get -y install libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get -y install git
sudo apt-get -y install curl
sudo apt-get -y install wireshark-dev

sudo pip3 install grpcio grpcio-tools
sudo pip3 install pyshark
sudo pip3 install scapy
sudo pip3 install mininet
sudo pip3 install aiohttp
sudo pip3 install python-socketio
# sudo pip3 install nest_asyncio
# sudo pip3 install flask
# sudo pip3 install flask_socketio
sudo pip3 install macaddress
sudo pip3 install pyroute2
SCRIPT


# ------------------------------------------------------------
# install mininet
# ------------------------------------------------------------
$install_mininet = <<SCRIPT
git clone https://github.com/mininet/mininet
cd mininet
# git tag  # list available versions
git checkout -b mininet-2.3.0 2.3.0  # or whatever version you wish to install
cd ..
# mininet/util/install.sh -n3fw
mininet/util/install.sh -a

sudo apt-get -y install openvswitch-switch
sudo service openvswitch-switch start
SCRIPT


# ------------------------------------------------------------
# install Lubutu Desktop
# ------------------------------------------------------------
$lubuntu_desktop = <<SCRIPT
sudo apt install -y --no-install-recommends lubuntu-desktop
SCRIPT

# ------------------------------------------------------------
# # vagrant configure version 2
# ------------------------------------------------------------
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    # vm name
    config.vm.hostname = $name + '.localhost'
    # ubuntu image
    config.vm.box = 'bento/ubuntu-18.04'
    # config.vm.box = 'bento/ubuntu-16.04'

    # network
    config.vm.network 'private_network', ip: '10.0.0.100'
    # port forward for ONOS
    config.vm.network 'forwarded_port', guest: 8181, host: 8181
    # port forward for tracing net web socket server
    config.vm.network 'forwarded_port', guest: 8888, host: 8888

    # share directory
    config.vm.synced_folder './', '/home/vagrant/share'

    # install package
    config.vm.provision 'shell', inline: $install_package
    config.vm.provision 'shell', inline: $install_mininet
    config.vm.provision 'shell', inline: $lubuntu_desktop


    # config virtual box
    config.vm.provider "virtualbox" do |vb|
        vb.name = $name
        vb.gui = true

        vb.cpus = 1
        vb.memory = "2048"
    
        vb.customize [
            "modifyvm", :id,
            "--vram", "16", 
            "--clipboard", "bidirectional", # clip board
            "--draganddrop", "bidirectional", # drag and drop
            "--ioapic", "off", # enable I/O APIC
            '--graphicscontroller', 'vmsvga',
            "--accelerate3d", "off",
            "--hwvirtex", "on",
            "--nestedpaging", "on",
            "--largepages", "on",
            "--pae", "off",
            '--audio', 'none',
            "--description", $description
        ]
    end
end
