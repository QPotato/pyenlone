"""
Basic example showing the use of API Key auth and teams.

To run this example, put a valid API Key ona file called "APIKEY".
"""
from pyenlone import V

with open("APIKEY") as input_file:
    apikey = input_file.read()[:-1]
v_api = V(apikey=apikey)

for team in v_api.list_teams():
    print(team.team)
    for member in v_api.team_details(team.teamid):
        print("\t" + member.agent)
