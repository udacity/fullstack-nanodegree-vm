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



-- Players table - this records the players and details about them.
CREATE TABLE players (
    player_id serial PRIMARY KEY,
    player_name text
);

-- Match table - records all the matches played by playerStandings
-- We will use this to record the matches played, and which user was the winner
CREATE TABLE matches (
    match_id serial PRIMARY KEY,
    winner_id int references players ON DELETE CASCADE,
    loser_id  int references players ON DELETE CASCADE
);



-- Records the stats about individual player statistics
CREATE TABLE playerScore (
    player_id int references players ON DELETE CASCADE,
    score int default 0,
    matches int default 0
);


CREATE TABLE playerResults (
    player_id int references players ON DELETE CASCADE,
    match_id int references matches ON DELETE CASCADE
);

CREATE OR REPLACE FUNCTION playerScore_create_id() RETURNS trigger AS $$
    BEGIN
        INSERT INTO playerScore(player_id) values (NEW.player_id);
        RETURN NEW;
    END;
$$
language plpgsql volatile;

CREATE TRIGGER playerScore_create_id
    AFTER INSERT ON players FOR EACH ROW EXECUTE PROCEDURE playerScore_create_id();

CREATE VIEW playerStandings as
    SELECT p.player_id, p.player_name, ps.score, ps.matches FROM players p,
    playerScore ps WHERE p.player_id = ps.player_id;
