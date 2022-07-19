from db.run_sql import run_sql
from models.league import League

def select_all():
    leagues = []
    sql = "SELECT * FROM leagues ORDER BY league_name"
    results = run_sql(sql)
    for result in results:
        league = League(result["league_name"], result["team_type"], result["id"])
        leagues.append(league)
    return leagues

def select(id):
    league = None
    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        league = League(result["league_name"], result["team_type"], result["id"])
    return league

def save(league):
    sql = "INSERT INTO leagues (league_name, team_type) VALUES (%s, %s) RETURNING id"
    values = [league.league_name, league.team_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    league.id = id

def update(league):
    sql = "UPDATE leagues SET league_name = %s WHERE id = %s"
    values = [league.league_name, league.team_type, league.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def league_table():
    return "Haha"