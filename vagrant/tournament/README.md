# To run Swiss Tournament Project you have to do the following.
# - Copy templates tournament.py, tournament.sql, and tournament_test.py into the folder vagrant/tournament folder.
# - SSH into the virtual machine using Vagrant SSH
# - From the vagrant/tournament folder in the shell, run psql -f tournament.sql to build the tables and view
# - From the same folder, run python tournament_test.py to test the schema.
# To run the test suite, :please, do the following.
# From a GitHub shell: 
# - cd fullstack/vagrant
# - vagrant up (you can turn off the VM with 'vagrant halt')
# - vagrant ssh (from here you can type 'exit' to log out)
# - cd /vagrant/tournament
# - psql -f tournament.sql
# - python tournament_results.py
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
