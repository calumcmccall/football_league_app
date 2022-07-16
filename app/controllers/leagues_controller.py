from crypt import methods
from flask import Blueprint, Flask, redirect, render_template, request

from models.league import League
import repositories.league_repository as league_repository

leagues_blueprint = Blueprint("leagues", __name__)

# INDEX
@leagues_blueprint.route("/leagues")
def leagues():
    leagues = league_repository.select_all()
    return render_template("/leagues/index.html", leagues=leagues)

# SHOW
@leagues_blueprint.route("/leagues/<id>")
def show_league(id):
    league = league_repository.select(id)
    return render_template("leagues/show.html", league=league)

# NEW
@leagues_blueprint.route("/leagues/new")
def new_league():
    return render_template("leagues/new.html")

# CREATE
@leagues_blueprint.route("/leagues", methods=["POST"])
def create_league():
    league_name = request.form['league_name']
    new_league = League(league_name)
    league_repository.save(new_league)
    return redirect("/leagues")

# EDIT
@leagues_blueprint.route("/leagues/<id>/edit")
def edit_league(id):
    league = league_repository.select(id)
    return render_template("leagues/edit.html", league=league)

# UPDATE
@leagues_blueprint.route("/leagues/<id>", methods=["POST"])
def update_league(id):
    league_name = request.form["league_name"]
    league = League(league_name, id)
    league_repository.update(league)
    return redirect("/leagues")

# DELETE
@leagues_blueprint.route("/leagues/<id>/delete", methods=["POST"])
def delete_league(id):
    league_repository.delete(id)
    return redirect("/leagues")