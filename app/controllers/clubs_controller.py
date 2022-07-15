from flask import Blueprint, Flask, redirect, render_template, request

from models.club import Club
import repositories.club_repository as club_repository

clubs_blueprint = Blueprint("clubs", __name__)

# INDEX
@clubs_blueprint.route("/clubs")
def clubs():
    clubs = club_repository.select_all()
    return render_template("clubs/index.html", clubs=clubs)

# NEW
@clubs_blueprint.route("/clubs/new")
def new_club():
    return render_template("clubs/new.html")

# CREATE
@clubs_blueprint.route("/clubs", methods=["POST"])
def create_club():
    club_name = request.form['club_name']
    new_club = Club(club_name)
    club_repository.save(new_club)
    return redirect("/clubs")

# EDIT
@clubs_blueprint.route("/clubs/<id>/edit")
def edit_club(id):
    club = club_repository.select(id)
    return render_template("clubs/edit.html", club=club)

# UPDATE
@clubs_blueprint.route("/clubs/<id>", methods=["POST"])
def update_club(id):
    club_name = request.form["club_name"]
    club = Club(club_name, id)
    club_repository.update(club)
    return redirect("/clubs")

# DELETE
@clubs_blueprint.route("/clubs/<id>/delete", methods=["POST"])
def delete_club(id):
    club_repository.delete(id)
    return redirect("/clubs")