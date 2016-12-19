-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches;

CREATE DATABASE tournament;
CREATE TABLE players (
    id serial UNIQUE primary key,
    name text
    );
CREATE TABLE matches (
    winner integer REFERENCES players,
    loser integer REFERENCES players,
    primary key (winner, loser)
    );
