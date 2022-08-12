import os

def installMysql():
    os.system('wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm')
    os.system('md5sum mysql80-community-release-el7-3.noarch.rpm')
    os.system('rpm -ivh mysql80-community-release-el7-3.noarch.rpm')
    os.system('rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022')
    os.system('yum update -y')
    os.system('yum install mysql-server -y')
    os.system('systemctl enable mysqld')
    os.system('systemctl start mysqld')
    os.system('systemctl status mysqld')

installMysql()
