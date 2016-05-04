-- Clear out any previous DB.
DROP DATABASE IF EXISTS tournament;

-- Create DB.
CREATE DATABASE tournament;

-- Connect to the DB before creating tables.
\c
 tournament;

-- Create table for players.
CREATE TABLE players (
id serial PRIMARY KEY,
name text NOT NULL
);

-- Create table for games.
CREATE TABLE matches(
id serial PRIMARY KEY,
winner INT REFERENCES players(id) ON DELETE CASCADE,
loser INT REFERENCES players(id) ON DELETE CASCADE
);

-- Create view to show standings.
CREATE VIEW standings AS
SELECT players.id,
players.name,
COUNT(matches.winner = players.id) AS wins,
COUNT(matches.*) AS games
FROM players LEFT JOIN matches
ON players.id = matches.winner OR
players.id = matches.loser
GROUP BY players.id, players.name
ORDER BY wins DESC;
