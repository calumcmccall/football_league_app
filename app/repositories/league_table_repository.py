from db.run_sql import run_sql
from models.league_table import LeagueTable

def select(id):
    this_league_table = []
    sql = "SELECT * FROM league_tables WHERE league_id=%s"
    values=[id]
    results = run_sql(sql, values)
    for result in results:
        result = results[0]
        this_league_table = LeagueTable.calculate_table(result)

    return this_league_table

def save(league_table):
    sql = "INSERT INTO league_tables (league_id, team_id, played, won, drawn, lost, gf, ga, gd, points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    values = [league_table.league_id, league_table.team_id, league_table.played, league_table.won, league_table.drawn, league_table.lost, league_table.gf, league_table.ga, league_table.gd, league_table.points]
    results = run_sql(sql, values)
    id = results[0]["id"]
    league_table.id = id