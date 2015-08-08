-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- prep: CREATE DATABASE tournament;

-- Players Table
CREATE TABLE Players (
	id SERIAL primary key,
	name varchar(255)
);

-- Matches Table
CREATE TABLE Matches (
	id SERIAL primary key,
	player int references Players(id),
	opponent int references Players(id),
	result int
);

-- Wins View shows number of wins for each Player
CREATE VIEW Wins AS
	SELECT Players.id, COUNT(Matches.opponent) AS n 
	FROM Players
	LEFT JOIN (SELECT * FROM Matches WHERE result>0) as Matches
	ON Players.id = Matches.player
	GROUP BY Players.id;

-- Count View shows number of matches for each Player
CREATE VIEW Count AS
	SELECT Players.id, Count(Matches.opponent) AS n 
	FROM Players
	LEFT JOIN Matches
	ON Players.id = Matches.player
	GROUP BY Players.id;

-- Standings View shows number of wins and matches for each Player
CREATE VIEW Standings AS 
	SELECT Players.id, Players.name, Wins.n as wins, Count.n as matches 
	FROM Players, Count, Wins
	WHERE Players.id = Wins.id and Wins.id = Count.id;

-- Standings OMW shows number of "Opponent Match Wins" for each Player
-- CREATE VIEW OMW AS
-- 	SELECT Players.id, sum(Standings.wins) as n
-- 	FROM Players,Standings,Matches
-- 	WHERE Players.id = Matches.player
-- 	AND Matches.opponent = Standings.id
-- 	Group by Players.id;