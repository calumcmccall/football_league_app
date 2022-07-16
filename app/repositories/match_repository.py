from db.run_sql import run_sql
from models.match import Match

import repositories.match_day_team_repository as match_day_team_repository
import repositories.league_repository as league_repository

def select_all():
    matches = []
    sql = "SELECT * FROM matches"
    results = run_sql(sql)
    for result in results:
        home_team = match_day_team_repository.select(result["home_team"])
        away_team = match_day_team_repository.select(result["away_team"])
        league = league_repository.select(result["league_id"])
        match = Match(home_team, away_team, result["home_team_score"], result["away_team_score"], league, result["id"])
        matches.append(match)
    return matches

def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        home_team = match_day_team_repository.select(result["home_team"])
        away_team = match_day_team_repository.select(result["away_team"])
        league = league_repository.select(result["league_id"])
        match = Match(home_team, away_team, result["home_team_score"], result["away_team_score"], league, result["id"])
    return match

def save(match):
    sql = "INSERT INTO matches (home_team, away_team, home_team_score, away_team_score, league_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [match.home_team.id, match.away_team.id, match.home_team_score, match.away_team_score, match.league.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    match.id = id

def update(match):
    sql = "UPDATE matches SET (home_team, away_team, home_team_score, away_team_score, league_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [match.home_team, match.away_team, match.home_team_score, match.away_team_score, match.league_id, match.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)