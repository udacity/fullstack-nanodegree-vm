-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
create DATABASE tournament;

\c tournament;
DROP TABLE IF EXISTS players;
CREATE TABLE players(
	player_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	wins INTEGER DEFAULT 0,
	losses INTEGER DEFAULT 0
	);

DROP TABLE IF EXISTS matches;
CREATE TABLE matches(
	winner INTEGER REFERENCES players (player_id),
	loser INTEGER REFERENCES players (player_id),
	PRIMARY KEY (winner, loser)
	);