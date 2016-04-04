-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE DATABASE tournament;
\c tournament;
CREATE TABLE Players(
id serial,
name varchar,
wins int,
loses int
);

CREATE TABLE Matches(
id serial,
player1 int,
player2 int,
victor int DEFAULT 	0
);