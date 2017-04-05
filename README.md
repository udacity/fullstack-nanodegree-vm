rdb-fullstack
=============

Common code for the Relational Databases and Full Stack Fundamentals courses

This program creates an SQL database for a game tournament and comes with a tester
for inserting and removing names as well as tracking wins and losses. To run the program,
navigate to its directory in your command line and set up a vagrant server using the following two commands:

vagrant up

vagrant ssh

Then, you can set up the tournament database on a virtual server using the following one-step command:

psql -f tournament.sql

Or if you prefer, you can use the following command sequence

cd /vagrant/tournament

psql tournament

\i tournament.sql

\c tournament

\q

Finally, you can run the actual tournament program:

python tournament.py

Or run the tester:

python tournament_test.py

For more information on the command sequences, refer to Vagrant and PSQL command line
documentation:

https://www.vagrantup.com/docs/

https://www.postgresql.org/docs/
