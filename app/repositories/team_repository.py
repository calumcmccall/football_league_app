from db.run_sql import run_sql
from models.team import Team

from models.club import Club
import repositories.club_repository as club_repository

def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        club = club_repository.select(result["club_id"])
        team = Team(result["team_name"], club, result["id"])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        club = club_repository.select(result["club_id"])
        team = Team(result["team_name"], club, result["id"])
    return team

def save(team):
    sql = "INSERT INTO teams (team_name, club_id) VALUES (%s, %s) RETURNING id"
    values = [team.team_name, team.club.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    team.id = id

def update(team):
    sql = "UPDATE teams SET (team_name, club_id) = (%s, %s) WHERE id = %s"
    values = [team.team_name, team.club_id, team.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def clubs_in_league(team_type):
    clubs_in_league = []

    sql = "SELECT clubs.club_name FROM clubs INNER JOIN teams on clubs.id = teams.club_id WHERE teams.team_name LIKE %s"
    values = [team_type]
    
    results = run_sql(sql, values)

    for result in results:
        clubs_in_league.append(result["club_name"])

    return clubs_in_league

def clubs_and_teams_in_league(team_type):
    clubs_in_league = []

    sql = "SELECT clubs.club_name FROM clubs INNER JOIN teams on clubs.id = teams.club_id WHERE teams.team_name LIKE %s"
    values = [team_type]
    
    results = run_sql(sql, values)

    for result in results:
        clubs_in_league.append(result["club_name"])

    return clubs_in_league