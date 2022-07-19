from flask import Flask, render_template

from controllers.clubs_controller import clubs_blueprint
from controllers.matches_controller import matches_blueprint
from controllers.teams_controller import teams_blueprint
from controllers.leagues_controller import leagues, leagues_blueprint

import repositories.league_repository as league_repository
import repositories.club_repository as club_repository

app = Flask(__name__)

app.register_blueprint(clubs_blueprint)
app.register_blueprint(matches_blueprint)
app.register_blueprint(teams_blueprint)
app.register_blueprint(leagues_blueprint)

@app.route("/")
def main():

    all_clubs = club_repository.select_all()
    all_leagues = league_repository.select_all()

    return render_template('index.html', all_leagues=all_leagues, all_clubs=all_clubs)

if __name__ == '__main__':
    app.run(debug=True)