CREATE DATABASE videogames_sales;

\c videogames_sales;

CREATE TABLE videogames
(
    rank SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    platform TEXT NOT NULL,
    year INTEGER,
    genre TEXT NOT NULL,
    publisher TEXT,
    na_sales FLOAT DEFAULT 0,
    eu_sales FLOAT DEFAULT 0,
    jp_sales FLOAT DEFAULT 0,
    other_sales FLOAT DEFAULT 0,
    global_sales FLOAT DEFAULT 0
);

