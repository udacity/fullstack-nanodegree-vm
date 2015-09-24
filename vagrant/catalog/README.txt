To run the software, first install:
Python 2.7, Vagrant, and VirtualBox. Instructions can be found here: https://www.udacity.com/wiki/ud197/install-vagrant

Python 2.7: https://www.python.org/downloads/<br>
Vagrant: https://www.vagrantup.com/downloads.html<br>
VirtualBox: https://www.virtualbox.org/wiki/Downloads<br>

# Start Vagrant
1. Once all the software is installed, open a terminal
2. Start Vagrant: `vagrant up`
3. Connect to Vagrant: `vagrant ssh`
<br>
# Run Catalog app
1. Go into the project folder: `cd /vagrant/catalog`
2. Start PSQL: `psql`
3. Create the database: `\i database.sql`
4. Exit PSQL: `\q`
5. Set `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` in `auth.py` to your Client ID and Client Secret
6. Run the tests: `python application.py`