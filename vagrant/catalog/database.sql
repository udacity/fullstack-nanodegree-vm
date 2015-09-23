DROP DATABASE IF EXISTS catalog;
CREATE DATABASE catalog;
\c catalog;

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
  category TEXT PRIMARY KEY NOT NULL,
  noitems INTEGER DEFAULT 0
);

DROP TABLE IF EXISTS items;
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT REFERENCES categories NOT NULL,
  descrip TEXT NOT NULL
);

-- UPDATE categories SET noitems = 1 WHERE category = 'Basketball'