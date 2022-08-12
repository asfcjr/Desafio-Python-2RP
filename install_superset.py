import os

def runsuperset():
    os.system('git clone https://github.com/apache/superset.git')
    os.system('docker compose -f /vagrant/superset/docker-compose-non-dev.yml pull')
    os.system('docker compose -f /vagrant/superset/docker-compose-non-dev.yml up')

runsuperset()