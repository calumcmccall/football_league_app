from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository
import repositories.club_repository as club_repository

teams_blueprint = Blueprint("teams", __name__)

# INDEX
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

# NEW
@teams_blueprint.route("/teams/new")
def new_team():
    clubs = club_repository.select_all()
    return render_template("teams/new.html", clubs=clubs)

# CREATE
@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    team_name = request.form["team_name"]
    club_id = request.form["club_id"]
    club = club_repository.select(club_id)
    new_team = Team(team_name, club)
    team_repository.save(new_team)
    return redirect("/teams")

# EDIT
@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    clubs = club_repository.select_all()
    return render_template("teams/edit.html", team=team, clubs=clubs)

# UPDATE
@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    team_name = request.form["team_name"]
    club_id = request.form["club_id"]
    club = club_repository.select(club_id)
    team = Team(team_name, club, id)
    team_repository.update(team)
    return redirect("/teams")

# DELETE
@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect("/teams")