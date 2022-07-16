from flask import Blueprint, Flask, redirect, render_template, request

from models.match import Match
import repositories.match_repository as match_repository

matches_blueprint = Blueprint("matches", __name__)

# INDEX
@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches=matches)

# new
@matches_blueprint.route("/matches/new")
def new_match():
    return render_template("matches/new.html")