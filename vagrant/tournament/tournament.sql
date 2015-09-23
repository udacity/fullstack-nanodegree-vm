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

-- Tournamanet table - generates a new ID, and we will return that when called
CREATE TABLE tournament (
    tournament_id serial PRIMARY KEY,
    tournament_name text DEFAULT "Udacity Tournament"
);

-- Players table - this records the players and details about them.
CREATE TABLE players (
    player_id serial PRIMARY KEY,
    tournament_id int references tournament ON DELETE CASCADE,
    player_name text
);

-- Records the stats about individual player statistics
CREATE TABLE matches (
    player_id int references players ON DELETE CASCADE,
    tournament_id int references tournament ON DELETE CASCADE,
    score int default 0,
    played int default 0
);

CREATE OR REPLACE FUNCTION matches_create_id() RETURNS trigger AS $$
    BEGIN
        INSERT INTO matches(player_id) values (NEW.player_id);
        RETURN NEW;
    END;
$$
language plpgsql volatile;

CREATE TRIGGER matches_create_id
    AFTER INSERT ON players FOR EACH ROW EXECUTE PROCEDURE matches_create_id();

CREATE VIEW playerStandings as
    SELECT p.player_id, p.player_name, m.score, m.played FROM players p,
    matches m WHERE p.player_id = m.player_id;
