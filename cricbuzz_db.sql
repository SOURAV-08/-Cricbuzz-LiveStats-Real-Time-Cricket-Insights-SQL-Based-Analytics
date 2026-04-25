-- Create Players Table
CREATE TABLE Players (
    player_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    role VARCHAR(50),
    batting_style VARCHAR(50),
    bowling_style VARCHAR(50)
);

--  Create Matches Table
CREATE TABLE Matches (
    match_id SERIAL PRIMARY KEY,
    season VARCHAR(10),
    match_date DATE,
    venue VARCHAR(150),
    team_1 VARCHAR(100),
    team_2 VARCHAR(100),
    toss_winner VARCHAR(100),
    winner VARCHAR(100),
    margin_value INT,
    margin_type VARCHAR(20)
);

--  Create Deliveries Table
CREATE TABLE Deliveries (
    delivery_id SERIAL PRIMARY KEY,
    match_id INT REFERENCES Matches(match_id),
    inning INT,
    batting_team VARCHAR(100),
    batsman_id INT REFERENCES Players(player_id),
    non_striker_id INT REFERENCES Players(player_id),
    bowler_id INT REFERENCES Players(player_id),
    runs_scored INT,
    extra_runs INT,
    is_wicket BOOLEAN DEFAULT FALSE,
    dismissal_kind VARCHAR(50)
);