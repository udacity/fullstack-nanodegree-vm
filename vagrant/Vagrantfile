# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provision "shell", path: "pg_config.sh"
  config.vm.box = "hashicorp/precise32"
  # config.vm.box = "ubuntu/trusty32"
  config.vm.boot_timeout = 600
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 80, host: 1050
  config.vm.network "forwarded_port", guest: 5000, host: 5000
end
