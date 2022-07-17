DROP TABLE IF EXISTS match_day_teams;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS clubs;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS leagues;

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    league_name VARCHAR(255),
    team_type VARCHAR(255)
);

CREATE TABLE clubs (
    id SERIAL PRIMARY KEY,
    club_name VARCHAR(255)
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name VARCHAR(255),
    club_id INT REFERENCES clubs(id)
);

CREATE TABLE match_day_teams (
    id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id)
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    home_team INT REFERENCES match_day_teams(id),
    away_team INT REFERENCES match_day_teams(id),
    home_team_score INT,
    away_team_score INT,
    league_id INT REFERENCES leagues(id)
);