# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.define "teste-zeppelin" do |master|
      master.vm.box = "centos/7"
      master.vm.hostname = "teste-zeppelin"
      master.disksize.size = "50GB"
      master.vm.network "public_network", bridge: "eth0", ip: "192.168.0.28"
      master.vm.provision "shell", path: "master.sh"
      master.vm.provision "file", source: "./create_users.py", destination: "~"
      master.vm.provision "file", source: "./zeppelin.service", destination: "/etc/systemd/system"
      master.vm.provider "virtualbox" do |vb|
        vb.memory = "4096"
        vb.cpus = "2"
      end  
    end
end