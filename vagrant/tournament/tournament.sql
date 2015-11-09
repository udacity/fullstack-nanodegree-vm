-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.




-- Things below this code is written by Bret Wagner, Original code unless
-- stated otherwise.
-- kill connection to old database and reset
\c vagrant
-- drop database tournament;
-- begin new database

create database tournament;

\c tournament;

create table players
(
    
    PlayerID serial primary key, 
--    FirstName text not null,
--    LastName text not null,
    name text not null,
--    Rank INTEGER,
    Wins INTEGER default 0,
    Matches INTEGER default 0,
    OppWins INTEGER default 0,
    byeWeek INTEGER default 0

);


create table matches(
    mID serial primary key,
    pid1 int,
    name1 text,
    pid2 int,
    name2 text
    );
    
create table records (
    matchid serial primary key,
    winner int,
    loser int
    );


