DROP DATABASE IF EXISTS entries;
CREATE DATABASE entries;
\c entries;

DROP TABLE IF EXISTS entries;
CREATE TABLE entries (
  autoincrement SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  text TEXT NOT NULL
);