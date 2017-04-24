#Swiss style tournament

A Swiss style tournament which creates players and tourments and matches them agaisnt each other. 

#Instuctions
1. install vagrant using Vagrentfile.
2. ssh to vagrant machine
3. Create database scheme by changing to tournament directory cd /vagrant/tournament
4. start psql
5. import sql '\i tournament.sql'
6. quit psql '\q'
7. launch unit testing file from inside tournament directory "python tournament_test.py"
