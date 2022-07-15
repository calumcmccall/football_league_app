from cProfile import run
from db.run_sql import run_sql
from models.club import Club

def select_all():
    clubs = []
    sql = "SELECT * FROM clubs"
    results = run_sql(sql)
    for result in results:
        club = Club(result["club_name"], result["id"])
        clubs.append(club)
    return clubs

def save(club):
    sql = "INSERT INTO clubs (club_name) VALUES (%s) RETURNING id"
    values = [club.club_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    club.id = id

def delete(id):
    sql = "DELETE FROM clubs WHERE id = %s"
    values = [id]
    run_sql(sql, values)