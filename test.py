from espn_api.football import League
import requests
#api is from github at the following link
#https://github.com/cwendt94/espn-api

espn_s2Val = 'AECHGftw9BiP%2BQJI9I5ywjd004jSxZDQrNDg0EpHiJJRVNhhG%2FGHfUCqCIwoJOH0A4RWs%2BLV2LHvFuy%2BHpjaAHUIiM1OWggDpy56grpSgDMIQhO1ZPyzF9zjvUkJ1mxuTk%2FiIdY4VL1TPuSYERRNoDiK%2B0QtuHKp4lfMjsqGozv5Y%2Fecf1FyAx%2Fw0wjq0VWrbooQS2WaOGi0FC5DZAXEcxXgn1Ixc07GEd3ZRXryvYdpyxuJJGOXMvHpDJ%2B2NdmvVIM%3D'
espn_swidVal = '{8ADCD598-EF97-4F8F-9983-D8FE222E1248}'
league_id = 172798
year = 2013

url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + \
    str(league_id) + "?seasonId=" + str(year)
#importing league with cookies from fantasy.espn.com, have to use
#espn_s2 and swid for private leagues
league = League(league_id=172798, year=2022, espn_s2=espn_s2Val, swid=espn_swidVal)

print (league.scoreboard(2)[0].home_score)
print (league.box_scores(2))