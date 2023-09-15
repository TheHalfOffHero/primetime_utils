from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from utilities import *

league = getLeague(2022)
matchupData = getMatchupWeek(league, 15)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', matchupData=matchupData)

if __name__ == "__main__":
  app.run(debug=True)