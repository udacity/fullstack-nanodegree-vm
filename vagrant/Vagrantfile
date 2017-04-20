# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial32"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get upgrade
    apt-get -qqy install make python3-pip
    apt-get -qqy install postgresql
    pip3 install --upgrade pip
    pip3 install flask packaging oauth2client redis passlib flask-httpauth
    pip3 install sqlalchemy flask-sqlalchemy psycopg2 bleach
    su postgres -c 'createuser -dRS ubuntu'
    su ubuntu -c 'createdb'
    su ubuntu -c 'createdb forum'
    su ubuntu -c 'psql forum -f /vagrant/forum/forum.sql'

    vagrantTip="[35m[1mThe shared directory is located at /vagrant\\nTo access your shared files: cd /vagrant[m"
    echo -e $vagrantTip > /etc/motd

    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make
    make install
  SHELL
end
