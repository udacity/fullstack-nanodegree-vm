-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE "tournament";
DROP TABLE "player_names";
DROP TABLE "matches";

CREATE TABLE tournament(match_id SERIAL PRIMARY KEY, player_id int NOT NULL);

CREATE TABLE player_names(player_id SERIAL PRIMARY KEY, player_name TEXT NOT NULL, wins int NOT NULL, matches int NOT NULL);

CREATE TABLE matches(match_id SERIAL PRIMARY KEY, winner_id int NOT NULL, loser_id INT NOT NULL);