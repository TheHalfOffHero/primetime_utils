from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from utilities import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  league = getLeague(2018)
  matchupData = getMatchupWeek(league, 15)
  
  if request.method == 'POST':
    matchupYear = int(request.form['matchupYear'])
    matchupWeek = int(request.form['matchupWeek'])
    
    league = getLeague(matchupYear)
    matchupData = getMatchupWeek(league, matchupWeek)
    
    return render_template('index.html', matchupData=matchupData)
  else:
    return render_template('index.html', matchupData=matchupData)

if __name__ == "__main__":
  app.run(debug=True)