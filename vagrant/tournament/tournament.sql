-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (
  player_id   SERIAL PRIMARY KEY,
  username    varchar(20) NOT NULL
);

CREATE TABLE standings (
  player_id   integer PRIMARY KEY,
  wins        integer DEFAULT 0,
  matches     integer DEFAULT 0
);

CREATE TABLE matchup (
  player_id_1   integer NOT NULL,
  username_1    varchar(20) NOT NULL,
  player_id_2   integer NOT NULL,
  username_2    varchar(20) NOT NULL
);
