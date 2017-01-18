-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE "tournament" CASCADE;
DROP TABLE "player_names" CASCADE;
DROP TABLE "matches" CASCADE;

CREATE TABLE tournament(match_id SERIAL PRIMARY KEY, winner_id int NOT NULL, loser_id INT NOT NULL);

CREATE TABLE player_names(player_id SERIAL PRIMARY KEY, player_name TEXT NOT NULL, wins int NOT NULL, matches int NOT NULL);

CREATE TABLE matches(match_id SERIAL PRIMARY KEY, winner_id int NOT NULL, loser_id INT NOT NULL);

--Count how many times each player has won
CREATE VIEW win_count AS 
SELECT player_names.player_id AS ID,
player_names.player_name AS Name,
COALESCE(COUNT(matches.winner_id),0) 
AS record
FROM player_names LEFT JOIN matches
ON player_names.player_id = matches.winner_id
GROUP BY player_names.player_id;
 
--Count how many times each player has lost
CREATE VIEW loss_count AS
SELECT player_names.player_id AS ID,
player_names.player_name AS Name,
COALESCE(COUNT(matches.loser_id),0) AS Record
FROM player_names LEFT JOIN matches
ON player_names.player_id = matches.loser_id
GROUP BY player_names.player_id;
 
--create view to count each player attend how many matches
CREATE VIEW matches_count AS
SELECT player_names.player_id AS ID,
player_names.player_name AS Name,
COUNT(matches.match_id) AS Played
FROM player_names LEFT JOIN matches
ON player_names.player_id = matches.winner_id or player_names.player_id = matches.loser_id
GROUP BY player_names.player_id;
  
--create view standing
CREATE VIEW standings AS
select matches_count.ID AS ID,
matches_count.Name AS Name,
COALESCE(win_count.Record,'0'),
matches_count.Played
FROM matches_count LEFT JOIN win_count 
ON win_count.ID = matches_count.ID 
ORDER BY COALESCE(win_count.Record) ASC;