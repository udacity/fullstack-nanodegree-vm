-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (
  player_id     SERIAL PRIMARY KEY,
  player_name   varchar(20) NOT NULL,
  wins          integer DEFAULT 0,
  matches       integer DEFAULT 0
);

CREATE TABLE matchup (
  id SERIAL PRIMARY KEY,
  winner INTEGER NOT NULL,
  loser INTEGER NOT NULL
);
