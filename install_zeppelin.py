import os

def installjava():
    os.system("yum update -y")
    os.system("yum install java-1.8.0-openjdk -y")
    os.system("java -version")

def exportvars():
    os.system('echo "export JAVA_HOME=/usr/java/jdk1.8.0_151" >> ~/.bash_profile')
    os.system('echo "export JRE_HOME=/usr/java/jdk1.8.0_151/jre" >> ~/.bash_profile')
    os.system('source ~/.bash_profile')
    os.system('echo $JAVA_HOME')

def installZeppelin():
    os.system('mv /vagrant/zeppelin.service /etc/systemd/system')
    os.system('wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz')
    os.system('tar xf zeppelin-*-bin-all.tgz -C /opt')
    os.system('mv /opt/zeppelin-*-bin-all /opt/zeppelin')
    os.system('adduser -d /opt/zeppelin -s /sbin/nologin zeppelin')
    os.system('chown -R zeppelin:zeppelin /opt/zeppelin')
    os.system('mv /vagrant/zeppelin-site.xml /opt/zeppelin/conf')
    os.system('chmod +x /opt/zeppelin/conf/zeppelin-site.xml')
    os.system('cp /opt/zeppelin/conf/zeppelin-env.sh.template /opt/zeppelin/conf/zeppelin-env.sh')
    os.system('/opt/zeppelin/bin/./zeppelin-daemon.sh start')


installjava()
exportvars()
installZeppelin()