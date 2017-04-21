DROP DATABASE if exists catalogs;
CREATE DATABASE catalogs;

\c catalogs;

CREATE TABLE categories(
    id serial primary key not null,
    name text not null
);

CREATE TABLE items(
    id serial primary key not null,
    name text not null,
    description text,
    cat_id int references categories(id)
);

INSERT INTO categories (name) VALUES('Soccer');
INSERT INTO categories (name) VALUES('Basketball');
INSERT INTO categories (name) VALUES('Baseball');
INSERT INTO categories (name) VALUES('Frisbee');
INSERT INTO categories (name) VALUES('Snowboarding');
INSERT INTO categories (name) VALUES('Rock Climbing');
INSERT INTO categories (name) VALUES('Foosball');
INSERT INTO categories (name) VALUES('Skating');
INSERT INTO categories (name) VALUES('Hockey');

INSERT INTO items (name,cat_id) VALUES('Stick',9);
INSERT INTO items (name,cat_id) VALUES('Googles',5);
INSERT INTO items (name,cat_id) VALUES('Snowboard',5);
INSERT INTO items (name,cat_id) VALUES('Two shingaurds',1);
INSERT INTO items (name,cat_id) VALUES('Shingaurds',1);
INSERT INTO items (name,cat_id) VALUES('Frisbee',4);
INSERT INTO items (name,cat_id) VALUES('Bat',3);
INSERT INTO items (name,cat_id) VALUES('Jersey',1);
INSERT INTO items (name,cat_id) VALUES('Soccer Cleats',1);

CREATE VIEW items_cat as select items.name as item,categories.name as category from items,categories where items.cat_id = categories.id;
