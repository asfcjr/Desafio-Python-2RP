#!/bin/sh

yum update -y
yum swapoff -a
yum install -y python3
yum install wget -y
python3 -V
yum install -y npm git
yum install -y yum-utils
yum install python3-pip -y
pip3 install --upgrade pip --user
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
export PATH=$PATH:/usr/local/bin
systemctl enable docker
systemctl start docker
chmod +x /vagrant/one-script-to-rule-them-all.sh