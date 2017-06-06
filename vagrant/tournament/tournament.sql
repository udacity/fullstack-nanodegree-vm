-- Baza
-- Tabele: Players, Matches, Rounds, PlayerStatistics

-- Players: id, nickname, wins, loses, ratio, standing
-- Matches: id, roundId, winnerId, loserId, draw
-- Rounds: id, wildcardPlayerId, playersAmount
-- PlayerStatistics: playerId, nickname, winner, runnerUp, third

CREATE DATABASE Tournament OWNER Vagrant;

CREATE TABLE Players (
	id SERIAL PRIMARY KEY,
	nickname varchar(40) NOT NULL CHECK (length(btrim(nickname)) > 0),
	wins integer DEFAULT 0,
	loses integer DEFAULT 0,
	ratio double precision DEFAULT 0.00,
	standing integer DEFAULT 0
	);

CREATE TABLE Matches (
	id SERIAL PRIMARY KEY,
	roundId integer,
	winnerId integer,
	loserId integer,
	draw boolean,
	);

CREATE TABLE Rounds (
	id integer PRIMARY KEY,
	wildcardPlayerId integer,
	playersAmount integer
	);

CREATE TABLE PlayerStatistics (
	playerId integer,
	nickname varchar(40),
	winner integer,
	runnerUp integer,
	third integer
	);


