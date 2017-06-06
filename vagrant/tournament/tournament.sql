-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament
CREATE TABLE players (
    id serial UNIQUE primary key,
    name text
    );
CREATE TABLE matches (
    id serial UNIQUE primary key,
    winner integer REFERENCES players,
    loser integer REFERENCES players
)
