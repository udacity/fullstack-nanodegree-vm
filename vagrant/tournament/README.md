Title: Swiss Tournament

Author: Jordan Shulman

This program is written in python and uses postgresql2. The tournament.sql file contain the table definitions for players and matchups, as well as the definition for a standings view. The tournament.py file contains the functions for populatin the tables and determining the swiss pairings. The tournament_test.py is run to test the functionality of the tournament.

In order to run this program, start up your vagant VM machine inside of the vagrant folder. Once the machine is running, change directories to /vagrant/torunament and run the command "psql CREATE DATABASE tournament". Next run the command "psql tournament" to enter the tournament database in psql. Once in psql, run the command "\i tournament.sql" to populate the database with your tables. To exit psql, enter the command "\q". Finally to test the program run the command "python tournament_test.py". 

