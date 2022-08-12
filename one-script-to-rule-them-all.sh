#!/bin/sh

python3 install_zeppelin.py
python3 create_users.py
python3 install_mysql.py
rm -rf /vagrant/mysql80-community-release-el7-3.noarch.rpm
rm -rf /vagrant/zeppelin-0.10.1-bin-all.tgz
python3 install_superset.py

# that's all folks