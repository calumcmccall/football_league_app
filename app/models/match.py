class Match:
    def __init__(self, home_team, away_team, home_team_score, away_team_score, league_id, id=None):
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_score = home_team_score
        self.away_team_score = away_team_score
        self.league_id = league_id
        self.id = id