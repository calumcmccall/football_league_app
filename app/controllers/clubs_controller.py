from flask import Blueprint, Flask, redirect, render_template, request

from models.club import Club
import repositories.club_repository as club_repository

clubs_blueprint = Blueprint("clubs", __name__)

# INDEX
@clubs_blueprint.route("/clubs")
def clubs():
    clubs = club_repository.select_all()
    return render_template("clubs/index.html", clubs=clubs)