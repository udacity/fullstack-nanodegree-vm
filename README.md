To run the software, first install:
Python 2.7, Vagrant, and VirtualBox. Instructions can be found here: https://www.udacity.com/wiki/ud197/install-vagrant

Python 2.7: https://www.python.org/downloads/
Vagrant: https://www.vagrantup.com/downloads.html
VirtualBox: https://www.virtualbox.org/wiki/Downloads

1. Once all the software is installed, open a terminal
2. Start Vagrant: vagrant up
3. Connect to Vagrant: vagrant ssh
4. Go into the project folder: cd /vagrant/tournament
5. Start PSQL: psql
6. Create the database: \i tournament.sql
7. Exit PSQL: \q
8. Run the tests: python tournament_test.py