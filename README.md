rdb-fullstack
=============

Common code for the Relational Databases and Full Stack Fundamentals courses

This program creates an SQL database for a game tournament and comes with a tester
for inserting and removing names as well as tracking wins and losses. To run the program,
navigate to its directory in your command line and set up a vagrant server. Then, you
can run it on a virtual server using the following command sequence:

vagrant up

vagrant ssh

cd /vagrant

(use cd command to navigate to the directory that has your files, usually /tournament)

psql tournament

\i tournament.sql

\c tournament

\q

python tournament_test.py

Note that tournament_test.py is a test program, while the actual tournament code is handled by
tournament.py.

For more information on the command sequence, refer to Vagrant and PSQL command line
documentation:

https://www.vagrantup.com/docs/

https://www.postgresql.org/docs/