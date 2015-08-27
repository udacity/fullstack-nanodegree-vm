-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- The tournament database
\c tournament;

-- Ability to drop database, tables and views
drop database if exists  tournament;
drop table if exists Players;
drop table if exists Matches;
drop view if exists Standings;
drop view if exists TotalMatches;
drop view if exists OponentWins;
drop view if exists TotalWins;
drop view if exists TotalLosses;
drop view if exists TotalDraws;

-- The players table
CREATE TABLE Players(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	date_created timestamp DEFAULT current_timestamp
);

-- The matches table, matches are played by two players
CREATE TABLE Matches(
	id PRIMARY KEY (Max((winner_id, loser_id),Min(winner_id,loser_id))
	winner_id INT references players(id) NOT NULL,
	loser_id INT references players(id),
	draw BOOLEAN Default False,
	match_date timestamp DEFAULT current_timestamp
);

-- Reporting player wins
CREATE VIEW TotalWins AS
SELECT Players.id, COUNT(Matches.winner_id) AS wins
FROM Players LEFT Join Matches
WHERE Matches.draw = False
ON Players.id = Matches.winner_id
GROUP BY Players.id
ORDER BY wins DESC

-- Reporting player losses
CREATE VIEW TotalLoses AS
SELECT Players.id, COUNT(Matches.loser_id) AS losses
FROM Players LEFT Join Matches
WHERE Matches.draw = False
ON Players.id = Matches.loser_id
GROUP BY Players.id
ORDER BY losses DESC

-- Reporting player draws
CREATE VIEW TotalDraws AS
SELECT Players.id, coalesce(COUNT(*), 0) AS draws
FROM Players LEFT Join Matches
WHERE Matches.draw = TRUE
ON Players.id = Matches.winner_id or Players.id = Matches.loser_id
GROUP BY Players.id
ORDER BY draws DESC

-- Reporting player standings based wins, losses, draws. Report is sorted by wins, oponent wins, and name.

