-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (id SERIAL PRIMARY KEY,
                      name TEXT);

CREATE TABLE matches (match_id SERIAL PRIMARY KEY,
                      winner INTEGER,
                      loser INTEGER,
                      draw BOOLEAN);
-- insert into players (id, name) VALUES (DEFAULT, 'Christian');
