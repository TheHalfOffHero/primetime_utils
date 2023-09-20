from espn_api.football import League
import requests
#api is from github at the following link
#https://github.com/cwendt94/espn-api
#This class is mostly a wrapper for the api so I don't have to keep creating new leagues

espn_s2Val = 'AECHGftw9BiP%2BQJI9I5ywjd004jSxZDQrNDg0EpHiJJRVNhhG%2FGHfUCqCIwoJOH0A4RWs%2BLV2LHvFuy%2BHpjaAHUIiM1OWggDpy56grpSgDMIQhO1ZPyzF9zjvUkJ1mxuTk%2FiIdY4VL1TPuSYERRNoDiK%2B0QtuHKp4lfMjsqGozv5Y%2Fecf1FyAx%2Fw0wjq0VWrbooQS2WaOGi0FC5DZAXEcxXgn1Ixc07GEd3ZRXryvYdpyxuJJGOXMvHpDJ%2B2NdmvVIM%3D'
espn_swidVal = '{8ADCD598-EF97-4F8F-9983-D8FE222E1248}'
league_id = 172798

'''
Variables:
  league_id: int
  year: int
  settings: Settings
  teams: List[Team]
  draft: List[Pick]
  current_week: int # current fantasy football week
  nfl_week: int
'''
# returns a league object
def getLeague(year):
  try:
    league = League(league_id, year, espn_s2Val, espn_swidVal)
    return league
  except:
    print(f'Unable to import League info for the year {year}')

'''
Variables
  home_team: Team
  home_score: int
  away_team: Team
  away_score: int
  is_playoff: bool
  matchup_type: str
'''
def getMatchupWeek(league, week):
  try:
    scoreboard = league.scoreboard(week)
    return scoreboard
  except:
    print(f'Unable to get scoreboard for week {week}')

''' 
    Gets all the scoreboards for the year and returns a list of all weeks
    There are 17 weeks in our fantasy season and we start at week 1
'''
def getMatchupYear(league):
  allMatchups = []
  for week in range(1, 17):
    currentMatchup = getMatchupWeek(league, week)
    allMatchups.append(currentMatchup)
  return allMatchups

league = getLeague(2021)
getMatchupWeek(league, 1)
print("done")