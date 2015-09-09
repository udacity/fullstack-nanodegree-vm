-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	wins INTEGER DEFAULT 0,
	matches INTEGER DEFAULT 0
);

CREATE TABLE matches (
	player1_id INTEGER NOT NULL REFERENCES players(id), -- REFERENCES makes sure the ID exists in the players table
	player2_id INTEGER NOT NULL REFERENCES players(id),
    CHECK (player2_id <> player1_id),
	winner_id INTEGER NOT NULL CHECK (
		winner_id = player1_id OR winner_id = player2_id
	), -- Winner can be player1 or player2
	PRIMARY KEY (player1_id, player2_id)
);

CREATE VIEW count_players AS SELECT COUNT(*) FROM players;