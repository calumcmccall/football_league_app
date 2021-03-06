from db.run_sql import run_sql
from models.club import Club
from models.team import Team

def select_all():
    clubs = []
    sql = "SELECT * FROM clubs ORDER BY club_name"
    results = run_sql(sql)
    for result in results:
        club = Club(result["club_name"], result["id"])
        clubs.append(club)
    return clubs

def select(id):
    club = None
    sql = "SELECT * FROM clubs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        club = Club(result["club_name"], result["id"])
    return club

def save(club):
    sql = "INSERT INTO clubs (club_name) VALUES (%s) RETURNING id"
    values = [club.club_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    club.id = id

def update(club):
    sql = "UPDATE clubs SET club_name = %s WHERE id = %s"
    values = [club.club_name, club.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM clubs WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def find_teams_for_club(id):
    teams = []

    sql = "SELECT teams.* FROM teams INNER JOIN clubs on teams.club_id = clubs.id WHERE club_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for result in results:
        team = Team(result["team_name"], select(id), result["id"])
        teams.append(team)

    return teams