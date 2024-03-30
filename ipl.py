import pandas as pd
import numpy as np



matches = pd.read_csv("IPL_Matches_2008_2022 - IPL_Matches_2008_2022.csv")

def teamsAPI():
    teams= list(set(list(matches['Team1']) + list(matches['Team2'])))
    teams_dict= {
        "teams":teams
    }
    return teams_dict


def teamVteamAPI(team_1, team_2):
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))

    team_1 = team_1.strip()
    team_2 = team_2.strip()

    # Normalize team names in the matches DataFrame
    matches['Team1'] = matches['Team1'].str.strip()
    matches['Team2'] = matches['Team2'].str.strip()
    matches['Team1'] = matches['Team1'].str.replace('\t', '')
    matches['Team2'] = matches['Team2'].str.replace('\t', '')

    # dataFrame based on team names
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    if team_1 in valid_teams and team_2 in valid_teams:
        temp_df = matches[((matches['Team1'] == team_1) & (matches['Team2'] == team_2)) |
                          ((matches['Team1'] == team_2) & (matches['Team2'] == team_1))]

        # total matches, matches won by each team, and draws
        total_matches = temp_df.shape[0]
        matches_won_team1 = temp_df['WinningTeam'].value_counts().get(team_1, 0)
        matches_won_team2 = temp_df['WinningTeam'].value_counts().get(team_2, 0)
        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
            'total_matches': str(total_matches),
            team_1: str(matches_won_team1),
            team_2: str(matches_won_team2),
            'draws': str(draws)
        }

    else:
        response = {'message':"Invalid team name"}

    return response




