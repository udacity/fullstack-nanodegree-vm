-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- I think in the tournament db should have two tables: t_player and t_match


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

DROP TABLE IF EXISTS t_player;
CREATE TABLE t_player (
  p_id        SERIAL PRIMARY KEY, --player id
  player_name VARCHAR(30) --player username
);


DROP TABLE IF EXISTS t_match;
CREATE TABLE t_match (
  m_id      SERIAL PRIMARY KEY,
  won_p_id  INT REFERENCES t_player (p_id), --winner:  the id number of the player who won
  lost_p_id INT REFERENCES t_player (p_id)--loser:  the id number of the player who lost
);