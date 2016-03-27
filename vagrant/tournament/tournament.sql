-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
--
-- Clean out any previous tournament databases.
DROP DATABASE IF EXISTS tournament;
--
-- Create database.
CREATE DATABASE tournament;
--
-- Connect to the DB before creating tables.
\c tournament;
--
-- Create table for payers.
CREATE TABLE players(id serial primary key, name text);
--
-- Create table for games.
CREATE TABLE matches(
game_id serial primary key, 
winner integer references players(id), 
loser integer references players(id), 
PRIMARY KEY (winner, loser)
);
--
-- Create a view to count total matches per player.
CREATE VIEW standings AS
SELECT players.id; players.name,

COUNT(matches.*)AS games
FROM players LEFT JOIN games
ON players.id = matches.winner OR 
players.id = matches.loser
GROUP BY players.id;
