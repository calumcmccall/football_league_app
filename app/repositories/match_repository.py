from db.run_sql import run_sql
from models.match import Match
import repositories.club_repository as club_repository

# def select_all():
#     matches = []
#     sql = "SELECT * FROM matches"
#     results = run_sql(sql)
#     for result in results:
#         match = Match()

# def save(match):
#     sql = "INSERT INTO matches () "