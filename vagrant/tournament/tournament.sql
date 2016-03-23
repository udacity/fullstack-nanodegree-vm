-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- ----------------------------
--  Database for tournaments
-- ----------------------------

DROP DATABASE IF EXISTS "tournament";
CREATE DATABASE "tournament";

DROP VIEW IF EXISTS player_count;
DROP VIEW IF EXISTS standings;
DROP VIEW IF EXISTS matches_played;
DROP VIEW IF EXISTS tournament;

-- ----------------------------
--  Table structure for tournaments
-- ----------------------------
DROP TABLE IF EXISTS "tournaments";
DROP SEQUENCE IF EXISTS tournament_id;
CREATE SEQUENCE tournament_id;
CREATE TABLE "tournaments" (
  "tournament_id" integer PRIMARY KEY DEFAULT nextval('tournament_id'),
  "tournament_name" text NOT NULL
);


-- ----------------------------
--  Table structure for players
-- ----------------------------
DROP TABLE IF EXISTS "players";
DROP SEQUENCE IF EXISTS player_id;
CREATE SEQUENCE player_id;
CREATE TABLE "players" (
	"player_id" integer PRIMARY KEY default nextval('player_id'),
	"player_name" text NOT NULL,
	"deleted" bool DEFAULT false,
	"tournament_id" integer NOT NULL
);

-- ----------------------------
--  Indexes structure for table players
-- ----------------------------
CREATE INDEX  "name" ON "players" USING btree(player_name COLLATE "default" "pg_catalog"."text_ops" ASC NULLS LAST);

-- ----------------------------
--  Table structure for matches
-- ----------------------------
DROP TABLE IF EXISTS "matches";
DROP SEQUENCE IF EXISTS match_id;
CREATE SEQUENCE match_id;
CREATE TABLE "matches" (
	"match_id" integer PRIMARY KEY default nextval('match_id'),
	"tournament_id" integer NOT NULL,
	"first_player_id" integer NOT NULL,
	"second_player_id" integer NOT NULL,
	"winner_id" integer NOT NULL
);

-- -------
--  Views
-- -------

-- -------------------------------------
--  View to return current tournament id
-- -------------------------------------

CREATE VIEW tournament AS 
 SELECT max(tournament_id) as current_tournament_id
   FROM tournaments;

-- -------------------------------------
--  View to return active players 
--  that are not deleted
-- -------------------------------------

CREATE VIEW player_count AS 
 SELECT count(player_id) count
   FROM players
    WHERE tournament_id = (
  		SELECT current_tournament_id 
  	  	  FROM tournament
  		)
    AND deleted = false;

-- -------------------------------------
--  View to return matches played
--  for the current tournament
-- -------------------------------------

CREATE VIEW matches_played AS 
 SELECT CASE WHEN count(*) > 0 THEN count(*) ELSE 0 END as count, p.player_id
   FROM players as p, matches as m
  WHERE (
  	p.player_id = first_player_id
  	OR
  	p.player_id = second_player_id
  	)
    AND p.tournament_id = (
  		SELECT current_tournament_id 
  	  	  FROM tournament
  		)
    GROUP BY player_id;

-- -------------------------------------
--  Display the current standings for
--  active players with any wins / games 
--  played in the current tournament
--  ordered by wins then randomly
-- -------------------------------------

 CREATE VIEW standings AS 
 SELECT p.player_id,
 		p.player_name,
 		CASE WHEN count(won.winner_id) > 0 THEN count(won.winner_id) ELSE 0 END as wins,
 		count(DISTINCT played.match_id) as matches
   FROM players p
  LEFT JOIN matches played ON (
  	p.player_id = played.first_player_id
  	OR
  	p.player_id = played.second_player_id
  	) AND p.tournament_id = (
  		SELECT current_tournament_id 
  	  	  FROM tournament
  		) 
  LEFT JOIN matches won ON p.player_id = won.winner_id
  AND p.tournament_id = (
      SELECT current_tournament_id 
          FROM tournament
      )
  WHERE p.deleted = false
    GROUP BY p.player_id
    ORDER BY wins DESC, random();

