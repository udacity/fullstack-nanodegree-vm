Full Stack Nanodegree Coursework
=============

This is the vagrnt virtual machine and included software as assigned by the Udacity Full Stack Nanodegree program. 
This code did contain some loose guides from Udacity which can be seen by viewing the original branch on github. 

Contained inside this fork you will find a tournament database application wtitten in python, a web forum and database, 
and a catalog database program which allows users to register and create their own lists of things

##########################

Tournament Database

##########################

To test the tournament, you will need to be in the vagrant VM, to do this open up your git bash and type 
$ vagrant up

once the system is up and you have another prompt in the terminal enter 
$ vagrant SSH

once this has been completed you will be logged into the vagrant virtual machine. to access the tournament files type 
$ cd /vagrant/tournament
$ psql
 \i tournament 
 \q
$ python tournament_test.py

At this time the tournament will run through the test and make sure that the basic functions all work.
At a later date there will be a front end built that allows users to create and manage their own tournaments
