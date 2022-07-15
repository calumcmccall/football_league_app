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