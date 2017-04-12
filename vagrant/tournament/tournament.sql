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
create table players (
    id serial primary key,
    name text
);


drop table if exists matches;
create table matches (
    id serial primary key, 
    winner int references players(id),
    loser int references players(id)
);


create view num_players as select count(*) from players;
create view num_matches as select count(*) from matches;

create view win_total as 
    select players.id, name,count(winner) as wins from players left join matches on players.id = matches.winner group by players.id;

create view matches_played as 
    select players.id, name,count(matches.winner) as total_matches from players left join matches on players.id in (matches.winner,matches.loser) group by players.id;


create view player_standing as
    select win_total.id,win_total.name,win_total.wins,matches_played.total_matches from matches_played join win_total on matches_played.id = win_total.id order by wins desc;


insert into players (name) values ('Waseem');
insert into players (name) values ('Wasim');
insert into players (name) values ('Ahmed');
insert into players (name) values ('Mohammad');

insert into matches (winner,loser) values (1,2);
insert into matches (winner,loser) values (1,2);
insert into matches (winner,loser) values (3,2);
insert into matches (winner,loser) values (2,1);
insert into matches (winner,loser) values (3,1);



