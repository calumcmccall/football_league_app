from models.league import League

import repositories.match_repository as match_repository
import repositories.team_repository as team_repository


class LeagueTable:
    @staticmethod
    def calculate_table(league):

        table = []

        teams = team_repository.clubs_and_teams_in_league(league.team_type)
        matches = match_repository.matches_for_league(league.id)

        for team in teams:

            this_team = team

            this_team = {
                "club": team,
                "played": 0,
                "wins": 0,
                "draws": 0,
                "losses": 0,
                "gf": 0,
                "ga": 0,
                "gd": 0,
                "points": 0
            }
            
            for match in matches:
                if match.home_team.team_id.club.club_name == team:
                    if match.home_team_score > match.away_team_score:
                        this_team["wins"] += 1
                    elif match.home_team_score == match.away_team_score:
                        this_team["draws"] += 1
                    else:
                        this_team["losses"] += 1
                    this_team["gf"] += match.home_team_score
                    this_team["ga"] += match.away_team_score
                elif match.away_team.team_id.club.club_name == team: 
                    if match.away_team_score > match.home_team_score:
                        this_team["wins"] += 1
                    elif match.away_team_score == match.home_team_score:
                        this_team["draws"] += 1
                    else:
                        this_team["losses"] += 1
                    this_team["gf"] += match.away_team_score
                    this_team["ga"] += match.home_team_score
            
            this_team["gd"] = this_team["gf"] - this_team["ga"]
            this_team["played"] = this_team["wins"] + this_team["draws"] + this_team["losses"]

            this_team["points"] = (this_team["wins"] * 3) + (this_team["draws"])

            table.append(this_team)

        sorted_table = sorted(table, key=lambda d: d['points'], reverse=True)

        return sorted_table

        # for match in matches:
        #     return match.home_team.team_id.club.club_name

        # return teams

# Get all teams in league

# Loop through teams in league

#   Get all matches for the team

#   Loop through matches for the team

#       If home_team = team

#           If they win + to wins

#           Else if they draw + to draws

#           Else + to loses

#       Else if away_team = team

#           If they win + to wins

#           Else if they draw + to draws

#           Else + to loses

#       Goals for +=

#       Goals against +=

#   Goal difference

#   Played = all matches they played

#   Points

#   Return list of dictionaries to template