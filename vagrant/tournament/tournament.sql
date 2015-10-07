-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE tournament;

CREATE DATABASE tournament;

\c tournament;

-- Tournamanet table - generates a new ID, and we will return that when called
CREATE TABLE tournament (
	tournament_id serial PRIMARY KEY
	,tournament_name TEXT DEFAULT 'Udacity Tournament'
	);

-- Players table - this records the players and details about them.
CREATE TABLE players (
	player_id serial PRIMARY KEY
	,tournament_id INT REFERENCES tournament ON DELETE CASCADE
	,player_name TEXT
	);

-- Records the stats about individual player statistics
CREATE TABLE matches (
	player_id INT REFERENCES players ON DELETE CASCADE
	,tournament_id INT REFERENCES tournament ON DELETE CASCADE
	,score INT DEFAULT 0
	,played INT DEFAULT 0
	);

--record matches played against each other - need to work out how to fold this into a view so we don't return previous matches.
CREATE TABLE played (
	match serial PRIMARY KEY
	,winner INT REFERENCES players ON DELETE CASCADE
	,loser INT REFERENCES players ON DELETE CASCADE
	);

CREATE
	OR REPLACE FUNCTION matches_create_id ()
RETURNS TRIGGER AS $$

BEGIN
	INSERT INTO matches (player_id)
	VALUES (NEW.player_id);

	RETURN NEW;
END;$$

LANGUAGE plpgsql volatile;

CREATE TRIGGER matches_create_id
AFTER INSERT ON players
FOR EACH ROW

EXECUTE PROCEDURE matches_create_id();

CREATE VIEW playerStandings
AS
SELECT p.tournament_id
	,p.player_id
	,p.player_name
	,m.score
	,m.played
FROM players p
	,matches m
WHERE p.player_id = m.player_id
ORDER BY - score
	,- played;

/******
 *  Test view to see if we can improve the results, but requires more work
 *  As well as a python loop to see if players have been matched previously.
 *  The first result for each player_id below should not have been seen, but
 *  there is some anomalous behaviour when there are 8 players or more.
 ******
*/
/*
CREATE VIEW pairings
AS
SELECT p.player_id AS player_id1
	,p.player_name AS player_name1
	,ps.player_id AS player_id2
	,ps.player_name AS player_name2
	,p.tournament_id as tournament_id
FROM playerstandings p
	,playerstandings ps
WHERE (
		p.player_id
		,ps.player_id
		) IN ( (SELECT p.player_id AS p1
			,ps.player_id AS p2
		FROM playerstandings p
		INNER JOIN playerstandings ps ON p.player_id < ps.player_id
			WHERE ((p.score/p.played) - (ps.score/ps.played)) < 1 ))
		  AND (p.player_id, ps.player_id) NOT IN (select winner, loser from played)
		 AND (p.player_id, ps.player_id) NOT IN (select loser, winner from played)
		 order by -(p.score);
		 */
