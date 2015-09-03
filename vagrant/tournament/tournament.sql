-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (
	_id SERIAL PRIMARY KEY CHECK (_id > -1),
	name TEXT NOT NULL
);

CREATE TABLE matches (
	player1_id INTEGER NOT NULL REFERENCES players(_id), -- REFERENCES makes sure the ID exists in the players table
	player2_id INTEGER NOT NULL REFERENCES players(_id),
    CHECK (player2_id <> player1_id),
	winner_id INTEGER NOT NULL CHECK (
		winner_id = player1_id OR winner_id = player2_id
	), -- Winner can be player1 or player2
	PRIMARY KEY (player1_id, player2_id)
);

CREATE VIEW count_players AS SELECT COUNT(*) FROM players;

CREATE VIEW get_last_id AS SELECT _id FROM players ORDER BY _id DESC LIMIT 1;