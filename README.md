FSND Tournament RDBMS Project
=============================

Vagrant setup to generate Swiss-system tournament pairings implemented
primarily in PostgreSQL with an interface provided in Python

Currently implementing all basic features required, the startup will be to
have both Vagrant and VirtualBox installed on the host PC

Change directory to vagrant
Execute the command:
vagrant up

This will spawn the instance, and initialise the database

Then execute the command
vagrant ssh

This will log you in to the vagrant ssh shell
cd /vagrant/tournament
Then you can execute the tests.
