-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE tournaments
(
	TID serial NOT NULL PRIMARY KEY,
	TDate date DEFAULT GETDATE(),
	TName varchar(30) NOT NULL,
	Enroll bool DEFAULT TRUE,
	Rounds int
);

CREATE TABLE players
(
	PID serial NOT NULL PRIMARY KEY,
	PName varchar(30)
);

CREATE TABLE registration
(
	RID serial NOT NULL PRIMARY KEY,
	TID integer FOREIGN KEY REFERENCES tournaments(TID),
	PID integer FOREIGN KEY REFERENCES players(PID),
	Wins int,
	Draws int,
	Losses int,
	Matches int
);

CREATE TABLE matches
(
	MatchID serial NOT NULL PRIMARY KEY,
	PlayerID integer FOREIGN KEY REFERENCES players(PID),
	OpponentID integer FOREIGN KEY REFERENCES players(PID),
	Wins int,
	Draws int,
	Losses int,
	Rount int
);
