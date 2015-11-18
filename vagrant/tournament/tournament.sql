-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database if exists tournament;
create database tournament;

\c tournament;
drop table if exists players;
create table players(
	player_id serial primary key,
	name varchar(50) not null,
	wins integer default 0,
	losses integer default 0
	);

drop table if exists matches;
create table matches(
	match_id serial primary key,
	winner integer references players (player_id),
	loser integer references players (player_id)
	);