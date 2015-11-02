-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.




-- Things below this code is written by Bret Wagner, Original code unless
-- stated otherwise.

create table players
(

    PlayerID INT,
    FirstName VARCHAR(200),
    LastName VARCHAR(200),
    Rank FLOAT(2),
    Wins INT,
    Matches INT,
    OppWins INT,
    byeWeek INT

);

create table global_players
(

    UID INT,
    FirstName VARCHAR(200),
    LastName VARCHAR(200),
    Rank INT,
    Wins INT,
    Matches INT,
    TotalMatches INT,
    OppWins INT,
    byeWeek INT,
    globalRank INT,
    email VARCHAR(200),
    phone VARCHAR(20),
    tournamentPoints INT

);

create table tournaments
(

    id INT,
    name VARCHAR(200)

    -- will add more columns to this table later as needed
);


