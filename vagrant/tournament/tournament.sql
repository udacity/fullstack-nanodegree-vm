-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE players;
DROP TABLE matchup;

CREATE TABLE players (
  player_id     SERIAL,
  player_name   varchar(20) NOT NULL,
  PRIMARY KEY (player_id)
);

CREATE TABLE matchup (
  id     SERIAL,
  winner INT,
  loser INT,
  PRIMARY KEY (id),
  FOREIGN KEY (winner) REFERENCES players(player_id),
  FOREIGN KEY (loser) REFERENCES players(player_id)
);

CREATE VIEW standings AS
SELECT players.player_id, players.player_name,
(SELECT count(matchup.winner)
    FROM matchup
    WHERE players.player_id = matchup.winner)
    AS wins,
(SELECT count(matchup.id)
    FROM matchup
    WHERE players.player_id = matchup.winner
    OR players.player_id = matchup.loser)
    AS matches
FROM players
ORDER BY wins DESC, matches DESC;
