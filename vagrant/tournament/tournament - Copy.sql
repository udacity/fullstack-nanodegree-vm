-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE matches(
    id SERIAL PRIMARY KEY,
    winner_id INTEGER REFERENCES players(id),
    loser_id INTEGER REFERENCES players(id)
);

CREATE VIEW player_wins AS
SELECT players.id, players.name, count(matches.winner_id) as wins,
FROM players LEFT JOIN matches
ON players.id = matches.winner_id
GROUP BY players.id
ORDER BY wins desc;

/*
CREATE VIEW player_losses AS
SELECT players.id, players.name, count(matches.loser_id) as losses,
FROM players LEFT JOIN matches
ON players.id = matches.loser_id
GROUP BY players.id
ORDER BY losses desc;

CREATE VIEW match_count AS
SELECT player_losses.id, player_losses.losses + player_wins.wins AS matches_played
FROM player_losses, player_wins
ON player_losses.id = player_wins.id
GROUP BY player_losses.id
ORDER BY matches_played desc;
*/
CREATE VIEW player_count AS
SELECT count(*)
FROM players;

INSERT INTO players (name) VALUES
('John D'),
('Jimmy L'),
('Jenny O'),
('Monty S'),
('Bobby E'),
('Beppy R'),
('Billy S'),
('Jenny W'),
('Monty I'),
('Bobby N'),
('Kai G'),
('Maike E'),
('Olaf B'),
('Leonard A'),
('Eva K'),
('Dylan D');