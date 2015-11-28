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
	TDate date DEFAULT now(),
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
	TID integer,
	PID integer,
	Wins int DEFAULT 0,
	Draws int DEFAULT 0,
	Losses int DEFAULT 0,
	Matches int DEFAULT 0
);

ALTER TABLE registration ADD CONSTRAINT FK_Registration_TID FOREIGN KEY (TID)
REFERENCES tournaments(TID);
ALTER TABLE registration ADD CONSTRAINT FK_Registration_PID FOREIGN KEY (PID)
REFERENCES players(PID);

CREATE TABLE matches
(
	MatchID serial NOT NULL PRIMARY KEY,
	PlayerID integer,
	OpponentID integer,
	Draw bool DEFAULT FALSE
);

ALTER TABLE matches ADD CONSTRAINT FK_MatchPlayer FOREIGN KEY (PlayerID) 
REFERENCES players(PID);
ALTER TABLE matches ADD CONSTRAINT FK_MatchOpponent FOREIGN KEY (OpponentID) 
REFERENCES players(PID);