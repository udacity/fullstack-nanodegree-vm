-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament;

-- Match table - records all the matches played by playerStandings
-- We will use this to record the matches played, and which user was the winner
CREATE TABLE matches (
    match_id serial PRIMARY KEY,
    winner_id int references players (player_id),
    loser_id  int references players (player_id),
    round 
);
-- Players table - this records the players and details about them.
CREATE TABLE players (
    player_id serial PRIMARY KEY,
    player_name varchar(128)
);

-- Records the stats about individual player statistics
CREATE TABLE playerStandings (
    player_id serial PRIMARY KEY,
    score int,
    matches int
);


CREATE TABLE playerResults (
    player_id int references players (player_id),
    match_id int references matches (match_id),

)

CREATE VIEW playerStandings as
    SELECT player_id, player_name
