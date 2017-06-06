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
drop view if exists OpponentWins;
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
	winner_id INT references players(id) NOT NULL,
	loser_id INT DEFAULT 0,
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
ON Players.id=Matches.winner_id OR Players.id=Matches.loser_id
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

-- Reporting opponent wins based on matches with players
CREATE VIEW OpponentMatchWins AS
SELECT Players.id, COALESCE(SUM(TotalWins.wins), 0) as opponent_wins
FROM
Players
LEFT JOIN (
SELECT winner_id AS player, loser_id AS opponent FROM Matches
UNION
SELECT winner_id AS opponent, loser_id AS player FROM Matches
) AS OpponentTable
ON Players.id = OpponentTable.player
LEFT JOIN TotalWins ON OpponentTable.opponent = TotalWins.id
GROUP BY Players.id
ORDER BY opponent_wins DESC;

-- Reporting player standings based wins, losses, draws. Report is sorted by wins, oponent wins, and name.
CREATE VIEW Standings AS
SELECT Players.id, Players.name, COALESCE(TotalWins.wins, 0), TotalMatches.total_matches
FROM Players
LEFT JOIN TotalWins ON Players.id=TotalWins.id
LEFT JOIN TotalMatches ON Players.id=TotalMatches.id
LEFT JOIN TotalDraws ON Players.id=TotalDraws.id
LEFT JOIN OpponentMatchWins ON Players.id=OpponentMatchWins.id
LEFT JOIN TotalLosses ON Players.id=TotalLosses.id
ORDER BY TotalWins.wins DESC, OpponentMatchWins.opponent_wins DESC, TotalDraws.draws DESC, TotalMatches.total_matches DESC, TotalLosses.losses ASC, Players.date_created DESC;

