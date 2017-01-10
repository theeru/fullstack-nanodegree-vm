-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Clear the database
DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS Players;

-- Create the tables
CREATE TABLE Players (
  name TEXT,
  id SERIAL PRIMARY KEY
);

CREATE TABLE Matches (
  winner INTEGER REFERENCES Players(id),
  loser INTEGER REFERENCES Players(id),
  PRIMARY KEY (winner, loser)
);
