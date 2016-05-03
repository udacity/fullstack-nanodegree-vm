# To run Swiss Tournament Project you have to do the following.
# 1. Copy templates tournament.py, tournament.sql, and tournament_test.py into the folder vagrant/tournament folder.
# 2. SSH into the virtual machine using Vagrant SSH
# 3. From the vagrant/tournament folder in the shell, run psql -f tournament.sql to build the tables and view
# 4. From the same folder, run python tournament_test.py to test the schema.
# To run the test suite (exercising all of the Python functions for the tournament database):
# From a GitHub shell:
# cd fullstack/vagrant
# 1.	vagrant up (you can turn off the VM with 'vagrant halt')
# 2.	vagrant ssh (from here you can type 'exit' to log out)
# 3.	cd /vagrant/tournament
# 4.	psql -f tournament.sql
# 5.	python tournament_results.py
# If all runs well you receive the following message:
# '''
# 1. Old matches can be deleted.
# 2. Player records can be deleted.
# 3. After deleting, countPlayers() returns zero.
# 4. After registering a player, countPlayers() returns 1.
# 5. Players can be registered and deleted.
# 6. Newly registered players appear in the standings with no matches.
# 7. After a match, players have updated standings.
# 8. After one match, players with one win are paired.
# Success!  All tests pass!
# '''
