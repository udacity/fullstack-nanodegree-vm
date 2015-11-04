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
drop database tournament;
-- begin new database

create database tournament;

\c tournament;

create table if not exists players
(
    
    PlayerID serial primary key, 
    FirstName text not null,
    LastName text not null,
    Rank INTEGER,
    Wins INTEGER,
    Matches INTEGER,
    OppWins INTEGER,
    byeWeek INTEGER

);

create table if not exists global_players
(

    UID INT,
    FirstName text,
    LastName text,
    Rank INT,
    Wins INT,
    Matches INT,
    TotalMatches INT,
    OppWins INT,
    byeWeek INT,
    globalRank INT,
    email text,
    phone text,
    tournamentPoints INT

);
create table if not exists matches(
    mID int,
    pid1 int,
    name1 text,
    pid2 int,
    name2 text
    );

create table if not exists tournaments
(

    id INT,
    name text

    -- will add more columns to this table later as needed
);


