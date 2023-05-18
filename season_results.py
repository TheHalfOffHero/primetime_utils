from espn_api.football import League
import requests
import pandas as pd
import numpy as np
import openpyxl

#api is from github at the following link
#https://github.com/cwendt94/espn-api

espn_s2Val = 'AECHGftw9BiP%2BQJI9I5ywjd004jSxZDQrNDg0EpHiJJRVNhhG%2FGHfUCqCIwoJOH0A4RWs%2BLV2LHvFuy%2BHpjaAHUIiM1OWggDpy56grpSgDMIQhO1ZPyzF9zjvUkJ1mxuTk%2FiIdY4VL1TPuSYERRNoDiK%2B0QtuHKp4lfMjsqGozv5Y%2Fecf1FyAx%2Fw0wjq0VWrbooQS2WaOGi0FC5DZAXEcxXgn1Ixc07GEd3ZRXryvYdpyxuJJGOXMvHpDJ%2B2NdmvVIM%3D'
espn_swidVal = '{8ADCD598-EF97-4F8F-9983-D8FE222E1248}'
league_id = 172798


#url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + \
#    str(league_id) + "?seasonId=" + str(year)


def print_matchup_data(year):
	
	#importing league with cookies from fantasy.espn.com, have to use
	#espn_s2 and swid for private leagues
	league = League(league_id=172798, year=year, espn_s2=espn_s2Val, swid=espn_swidVal)
	
	#print(league.box_scores(1))
	
	home_teams = []
	home_scores = []
	away_teams = []
	away_scores = []
	weeks = []
	
	for i in range(18):
		week = i
		matchups = league.scoreboard(week)
		num_matchups = len(matchups) #check the number of matchups for the week
		for x in range(min(5, num_matchups)):
			home_team = matchups[x].home_team
			home_team = str(home_team).replace("Team(","")
			home_team = str(home_team).replace(")","")
			home_teams.append(home_team)
		
			home_score = matchups[x].home_score
			home_scores.append(home_score)
		
			away_team = matchups[x].away_team
			away_team = str(away_team).replace("Team(","")
			away_team = str(away_team).replace(")","")
			away_teams.append(away_team)
		
			away_score = matchups[x].away_score
			away_scores.append(away_score)
			
			weeks.append(f"Week {week}")
	
	#Difference in scores, will use to determine the winner
	score_difference = list()
	for i in range(len(home_scores)):
		item = home_scores[i] - away_scores[i]
		score_difference.append(item)
	
	#Winning team
	winner = list()
	for i in range(len(home_teams)):
		if score_difference[i] > 0:
			winner.append(home_teams[i])
		elif score_difference[i] < 0:
			winner.append(away_teams[i])
		else:
			winner.append("TIE")
	
	#Formatting the data to be input into the cells with headers
	data = {'Week':weeks, 'Home Team':home_teams, 'Home Score':home_scores,\
				'Away Score':away_scores, 'Away Team':away_teams, \
				'Score_Difference': score_difference, 'Winner': winner}
	# Convert the data to a pandas DataFrame
	df = pd.DataFrame.from_dict(data, orient = 'index')
	
	df=df.transpose()

	#Convert the DataFrame to an Excel file
	df.to_excel(writer, sheet_name = f"{year} Data", index=False)
	
	#Resize columns to fit the data		
	workbook = writer.book
	worksheet = workbook[f"{year} Data"]
	for column in worksheet.columns:
		max_length = 0
		column = [cell for cell in column]
		for cell in column:
			try:
				if len(str(cell.value))> max_length:
					max_length = len(cell.value)
			except:
				pass
		adj_width = (max_length + 2)*1.2
		worksheet.column_dimensions[column[0].column_letter].width = adj_width

		
#Send the end of the year rosters into the Primetime spreadsheet
def team_rosters (year):
	
	#Get League for certain year
	league = League(league_id=172798, year=year, espn_s2=espn_s2Val, swid=espn_swidVal)
	
	#List of teams
	teams = league.teams
	#print(teams)
	
	roster_data = {}

	for team in teams:
		roster = team.roster
		roster_data[team] = roster
	
	# # Convert the data to a pandas DataFrame
	df = pd.DataFrame.from_dict(roster_data, orient = 'index')
	
	df=df.transpose()

	# #Convert the DataFrame to an Excel file
	df.to_excel(writer, sheet_name = f"{year} Rosters", index=False)
	
	#Resize columns to fit the data		
	workbook = writer.book
	worksheet = workbook[f"{year} Rosters"]
	for column in worksheet.columns:
		max_length = 0
		column = [cell for cell in column]
		for cell in column:
			try:
				if len(str(cell.value))> max_length:
					max_length = len(cell.value)
			except:
				pass
		adj_width = (max_length + 2)*1.2
		worksheet.column_dimensions[column[0].column_letter].width = adj_width
		
		
#Create a Pandas Excel writer using openpyxl as the engine
with pd.ExcelWriter('primetime_data.xlsx', engine = 'openpyxl') as writer:
	for year in range(2015,2024):
		print_matchup_data(year)
		team_rosters(year)
	
