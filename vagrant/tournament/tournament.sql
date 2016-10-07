-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


create database tournament;
\c tournament;
create table players (id serial, name text, rank int, matches int);
create table matches (winner int, loser int);