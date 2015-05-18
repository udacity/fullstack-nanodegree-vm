-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (id SERIAL PRIMARY KEY,
						name VARCHAR(64));

CREATE TABLE matches (id SERIAL PRIMARY KEY,
						winner_id INT REFERENCES players(id),
						loser_id INT REFERENCES players(id));

CREATE VIEW players_standings AS SELECT id, name, 
(SELECT COUNT(*) FROM matches WHERE winner_id = players.id) wins, 
(SELECT COUNT(*) FROM matches WHERE winner_id = players.id OR loser_id = players.id) matches 
FROM players
ORDER BY wins DESC;

CREATE VIEW players_wins AS 
SELECT row_number() OVER(ORDER BY wins DESC) as position, ps.id, ps.name, ps.wins
FROM (
	SELECT id, name, wins FROM players_standings
) AS ps;
