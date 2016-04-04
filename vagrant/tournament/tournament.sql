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
name varchar,
wins int DEFAULT 0,
loses int DEFAULT 0,
id serial
);

CREATE TABLE Matches(
id serial,
player1 int,
player2 int,
victor int DEFAULT 	0
);