-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Ability to drop database, tables and views
drop DATABASE if exists tournament;
drop table if exists Players;
drop table if exists Matches;
drop view if exists Standings;
drop view if exists TotalMatches;
drop view if exists OponentWins;
drop view if exists TotalWins;
drop view if exists TotalLosses;
drop view if exists TotalDraws;

-- The tournament database
CREATE DATABASE tournament;
\c tournament

-- The players table
CREATE TABLE Players(
	id serial  PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	date_created timestamp DEFAULT current_timestamp
);

-- The matches table, matches are played by two players
CREATE TABLE Matches(
	PRIMARY KEY(winner_id,loser_id),
	CONSTRAINT keys UNIQUE(winner_id,loser_id),
	winner_id INT references players(id) NOT NULL,
	loser_id INT references players(id),
	draw BOOLEAN Default False,
	match_date timestamp DEFAULT current_timestamp
);

-- Reporting player wins
CREATE VIEW TotalWins AS
SELECT Players.id, COALESCE(COUNT(Matches.winner_id), 0) AS wins
FROM Players LEFT JOIN  Matches
ON Players.id = Matches.winner_id
WHERE Matches.draw<>True
GROUP BY Players.id
ORDER BY wins DESC;

-- Reporting player losses
CREATE VIEW TotalLosses AS
SELECT Players.id, COALESCE(COUNT(Matches.loser_id), 0) AS losses
FROM Players LEFT JOIN Matches
ON Players.id = Matches.loser_id
WHERE Matches.draw<>True
GROUP BY Players.id
ORDER BY losses DESC;

-- Reporting player draws
CREATE VIEW TotalDraws AS
SELECT Players.id, COALESCE(COUNT(*), 0) AS draws
FROM Players LEFT JOIN Matches
ON Players.id = Matches.winner_id or Players.id = Matches.loser_id
WHERE Matches.draw=True
GROUP BY Players.id
ORDER BY draws DESC;

-- Reporting player matches
CREATE VIEW TotalMatches AS
SELECT Players.id, COALESCE(wins, 0) + COALESCE(losses, 0) + COALESCE(draws, 0) AS total_matches
FROM Players
LEFT JOIN TotalWins ON Players.id=TotalWins.id
LEFT JOIN TotalLosses ON Players.id=TotalLosses.id
LEFT JOIN TotalDraws ON Players.id=TotalDraws.id
ORDER BY total_matches DESC;

-- Reporting player standings based wins, losses, draws. Report is sorted by wins, oponent wins, and name.
CREATE VIEW Standings AS
SELECT Players.id, Players.name, COALESCE(TotalWins.wins, 0), TotalMatches.total_matches
FROM Players
LEFT JOIN TotalWins ON Players.id=TotalWins.id
LEFT JOIN TotalMatches ON Players.id=TotalMatches.id
ORDER BY TotalWins.wins DESC, TotalMatches.total_matches DESC, Players.date_created DESC;

