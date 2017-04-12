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

/*
   SWISS PAIRING LOGIC
   1. Select all even_rows ordered by number of wins
   2. Select all odd_rows ordered by number of wins
   3. Combine above two tables with corresponding rows to get the result

*/
 create view even_rows as 
    with cte as ( select row_number() over (order by wins desc) as row, * from player_standing)
    select * from cte where row%2=0;

create view odd_rows as 
    with cte as ( select row_number() over (order by wins desc) as row, * from player_standing)
    select * from cte where row%2!=0;

create view swiss_pair as 
    select odd_rows.id as id1 , odd_rows.name as name1 , even_rows.id as id2 , even_rows.name as name2 from odd_rows,even_rows where odd_rows.row = even_rows.row - 1; -- Get corresponding row



