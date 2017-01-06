-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Clear the database
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;

-- Create the tables
CREATE TABLE players (
  name TEXT,
  id SERIAL PRIMARY KEY
);

CREATE TABLE matches (
  winner INTEGER REFERENCES players(id),
  loser INTEGER REFERENCES players(id),
  PRIMARY KEY (winner, loser)
);
