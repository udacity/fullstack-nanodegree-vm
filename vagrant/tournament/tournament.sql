-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;
\c tournament
CREATE TABLE players (
    id serial UNIQUE primary key,
    name text
    );
CREATE TABLE matches (
    id serial UNIQUE primary key,
    winner integer REFERENCES players(id),
    loser integer REFERENCES players(id)
)
CREATE VIEW player_wins AS
SELECT players.id as id, players.name as name, count(matches.winner) as wins
FROM players LEFT JOIN matches
ON players.id = matches.winner
GROUP BY players.id

CREATE VIEW player_matches AS
SELECT players.id as id, count(matches.winner + matches.loser) as matches
FROM players LEFT JOIN matches
ON players.id = matches.winner or players.id = matches.loser
GROUP BY players.id
