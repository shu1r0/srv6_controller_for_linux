# vm name 
$name = "ubuntu-SRv6-dev"

# ------------------------------------------------------------
# Description
# ------------------------------------------------------------
$description = <<'EOS'
Windows Environment for OFP2V (OpenFlow Pipeline Processing Viewer)

Tools that need to be installed manually following:
* TShark

You may need vagrant plugin following:
* vagrant-vbguest


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
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get -y update

sudo apt-get -y install build-essential
sudo apt-get -y install sshpass
sudo apt-get -y install python3.8-dev python3.8
sudo apt-get -y install python3-pip

# python upgrade
# update-alternatives causes a bug
# sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 20
# sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 10
# sudo alternatives --auto python3

python3 -m pip install -U pip
sudo apt-get -y remove python-pexpect python3-pexpect

sudo apt-get -y install libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get -y install git
sudo apt-get -y install curl
sudo apt-get -y install wireshark-dev

#NOTE: Should is used venv???
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade pexpect
sudo pip3 install --upgrade lxml
sudo pip3 install grpcio grpcio-tools
sudo pip3 install pyshark
sudo pip3 install scapy
sudo pip3 install mininet
sudo pip3 install aiohttp
sudo pip3 install python-socketio
sudo pip3 install nest_asyncio
sudo pip3 install python-openflow
sudo pip3 install flask
sudo pip3 install flask_socketio
sudo pip3 install macaddress
sudo pip3 install pyroute2
SCRIPT

# ------------------------------------------------------------
# install Vue 3
# 
# References:
#    - https://linuxize.com/post/how-to-install-node-js-on-ubuntu-20-04/
# ------------------------------------------------------------
$install_vue = <<SCRIPT
sudo curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install -y nodejs

sudo chown -R vagrant /usr/lib/node_modules/
sudo npm install -g n
sudo npm install -g @vue/cli

sudo n install 10.16.0
SCRIPT


# ------------------------------------------------------------
# install mininet with bofuss
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
# install BOFUSS (build from source)
#@link https://github.com/CPqD/ofsoftswitch13
# ------------------------------------------------------------
$install_bofuss = <<SCRIPT
sudo apt-get install -y cmake libpcap-dev libxerces-c3.2 libxerces-c-dev libpcre3 libpcre3-dev flex bison pkg-config autoconf libtool libboost-dev

# Clone and build netbee
git clone https://github.com/netgroup-polito/netbee.git
cd netbee/src
cmake .
make
cd ../tools
cmake .
make
cd ../samples
cmake .
make
cd ..
sudo ./install.sh

# sudo apt-get install -y wireshark-dev
# sudo apt-get install -y scons
# export WIRESHARK=/usr/include/wireshark
SCRIPT

# ------------------------------------------------------------
# install ryu 
# Libraries dependent on ryu are added here as required
# ------------------------------------------------------------
$install_ryu = <<SCRIPT
sudo apt install -y python3-ryu
SCRIPT

# ------------------------------------------------------------
# install faucet
# Notes:
#   * faucet configuration `` /etc/faucet/faucet.yaml ``
#@link: https://docs.faucet.nz/en/latest/tutorials/first_time.html#package-installation
# ------------------------------------------------------------
$install_faucet = <<SCRIPT
sudo apt-get install -y curl gnupg apt-transport-https lsb-release
echo "deb https://packagecloud.io/faucetsdn/faucet/$(lsb_release -si | awk '{print tolower($0)}')/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/faucet.list
curl -L https://packagecloud.io/faucetsdn/faucet/gpgkey | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y faucet-all-in-one
SCRIPT

# ------------------------------------------------------------
# install ONOS
# ------------------------------------------------------------
$install_onos = <<ONOS
sudo apt install -y openjdk-11-jdk

cd /opt
sudo wget -c https://repo1.maven.org/maven2/org/onosproject/onos-releases/2.5.1/onos-2.5.1.tar.gz
sudo tar xzf onos-2.5.1.tar.gz
sudo mv onos-2.5.1 onos

sudo cp /opt/onos/init/onos.initd /etc/init.d/onos
sudo cp /opt/onos/init/onos.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable onos
ONOS

# ------------------------------------------------------------
#NOTE: I don't test
#@link https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
# ------------------------------------------------------------
$install_mongodb = <<SCRIPT
sudo apt-get install -y gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update -y
sudo apt-get install -y mongodb-org
# sudo systemctl start mongod
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
    # config.vm.provision 'shell', inline: $install_vue
    # config.vm.provision 'shell', inline: $install_onos


    # ssh config
    config.ssh.username = 'vagrant'
    config.ssh.password = 'vagrant'
    config.ssh.insert_key = false

    config.vbguest.auto_update = false

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

        vb.customize ["setextradata", :id, 
            "VBoxInternal2/SharedFoldersEnableSymlinksCreate/Folder_Name", "1"
        ]
    end
end
