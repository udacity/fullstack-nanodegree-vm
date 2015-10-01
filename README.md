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

You can then execute the standing tests by simply running:
python tournament_test.py

Alternatively there is a slightly extended test implementing a number of rounds
This is in short_test.py and has an 8 player swiss-style matching system

python short_test.py

** Additional functionality to be explored:
Explicitly test each match
Currently I am randomising the pairs that come back to try to avoid the first
player winning each round in the 8 player test, and I'm getting reliable results
but currently not happy with matches that come back.
