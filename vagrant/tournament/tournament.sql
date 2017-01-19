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

CREATE TABLE players(player_id SERIAL PRIMARY KEY, player_name TEXT NOT NULL);

CREATE TABLE matches(match_id SERIAL PRIMARY KEY, winner_id int REFERENCES players(player_id) ON DELETE CASCADE, loser_id INT REFERENCES players(player_id) ON DELETE CASCADE);

--Count how many times each player has won
CREATE VIEW win_count AS 
SELECT players.player_id AS ID,
players.player_name AS Name,
COALESCE(COUNT(matches.winner_id),0) 
AS record
FROM players LEFT JOIN matches
ON players.player_id = matches.winner_id
GROUP BY players.player_id;
 
--Count how many times each player has lost
CREATE VIEW loss_count AS
SELECT players.player_id AS ID,
players.player_name AS Name,
COALESCE(COUNT(matches.loser_id),0) AS Record
FROM players LEFT JOIN matches
ON players.player_id = matches.loser_id
GROUP BY players.player_id;
 
--create view to count each player attend how many matches
CREATE VIEW matches_count AS
SELECT players.player_id AS ID,
players.player_name AS Name,
COUNT(matches.match_id) AS Played
FROM players LEFT JOIN matches
ON players.player_id = matches.winner_id OR players.player_id = matches.loser_id
GROUP BY players.player_id;
  
--create standings view
CREATE VIEW standings AS
SELECT matches_count.ID AS ID,
matches_count.Name AS Name,
COALESCE(win_count.Record,'0'),
matches_count.Played
FROM matches_count LEFT JOIN win_count 
ON win_count.ID = matches_count.ID 
ORDER BY COALESCE(win_count.Record) ASC;