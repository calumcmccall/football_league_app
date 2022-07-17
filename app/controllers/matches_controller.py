from flask import Blueprint, Flask, redirect, render_template, request

from models.match import Match
from models.match_day_team import MatchDayTeam
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository
import repositories.match_day_team_repository as match_day_team_repository
import repositories.league_repository as league_repository

matches_blueprint = Blueprint("matches", __name__)

# INDEX
@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    teams = team_repository.select_all()
    return render_template("matches/index.html", matches=matches, teams=teams)

# NEW
@matches_blueprint.route("/matches/new")
def new_match():
    teams = team_repository.select_all()
    leagues = league_repository.select_all()
    return render_template("matches/new.html", teams=teams, leagues=leagues)

# CREATE
@matches_blueprint.route("/matches", methods=["POST"])
def create_match():
    home_team = team_repository.select(request.form["home_team"])
    home_team_for_match = MatchDayTeam(home_team.id)
    match_day_team_repository.save(home_team_for_match)

    away_team = team_repository.select(request.form["away_team"])
    away_team_for_match = MatchDayTeam(away_team.id)
    match_day_team_repository.save(away_team_for_match)


    home_team_score = request.form["home_team_score"]
    away_team_score = request.form["away_team_score"]
    
    league = league_repository.select(request.form["league"])
    new_match = Match(home_team_for_match, away_team_for_match, home_team_score, away_team_score, league)
    
    match_repository.save(new_match)
    return redirect("/matches")

# DELETE
@matches_blueprint.route("/matches/<id>/delete", methods=["POST"])
def delete_match(id):
    match_repository.delete(id)
    return redirect("/matches")