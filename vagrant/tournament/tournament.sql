-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

#start with clean database each time
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament
create table players (id int serial PRIMARY KEY, name text, rank int, matches int);
create table matches (match int serial PRIMARY KEY, winner int references players(id), loser int references players(id));