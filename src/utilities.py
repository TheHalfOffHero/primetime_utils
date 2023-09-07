from espn_api.football import League
import requests
#api is from github at the following link
#https://github.com/cwendt94/espn-api

espn_s2Val = 'AECHGftw9BiP%2BQJI9I5ywjd004jSxZDQrNDg0EpHiJJRVNhhG%2FGHfUCqCIwoJOH0A4RWs%2BLV2LHvFuy%2BHpjaAHUIiM1OWggDpy56grpSgDMIQhO1ZPyzF9zjvUkJ1mxuTk%2FiIdY4VL1TPuSYERRNoDiK%2B0QtuHKp4lfMjsqGozv5Y%2Fecf1FyAx%2Fw0wjq0VWrbooQS2WaOGi0FC5DZAXEcxXgn1Ixc07GEd3ZRXryvYdpyxuJJGOXMvHpDJ%2B2NdmvVIM%3D'
espn_swidVal = '{8ADCD598-EF97-4F8F-9983-D8FE222E1248}'
league_id = 172798

def getLeague(year):
  try:
    league = League(league_id, year, espn_s2Val, espn_swidVal)
    return league
  except:
    print(f'Unable to import League info for the year {year}')
    
getLeague(2022)