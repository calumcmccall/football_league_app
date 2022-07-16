from db.run_sql import run_sql
from models.match_day_team import MatchDayTeam

def select_all():
    match_day_teams = []
    sql = "SELECT * FROM match_day_teams ORDER BY id"
    results = run_sql(sql)
    for result in results:
        match_day_team = MatchDayTeam(result["team_id"], result["id"])
        match_day_teams.append(match_day_team)
    return match_day_teams

def select(id):
    match_day_team = None
    sql = "SELECT * FROM match_day_teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        match_day_team = MatchDayTeam(result["team_id"], result["id"])
    return match_day_team

def save(match_day_team):
    sql = "INSERT INTO match_day_teams (team_id) VALUES (%s) RETURNING id"
    values = [match_day_team.team_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    match_day_team.id = id