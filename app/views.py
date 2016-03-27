from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title = 'Home')

@app.route('/draft')
def draft():
    teams = 'add_teams_here' ## Add teams here
    teams_two = [['Oakland Athletics', 2, 2, 4], ['Los Angeles Dodgers', 4, 1, 4]]
    return render_template('draft.html',
                           title = 'Draft Prep',
                           teams = teams_two)

@app.route('/managers')
def managers():
    return render_template('manager_index.html',
                           title = 'Managers')

@app.route('/standings')
def standings():
    return "Under construction! Stay tuned for some kick-ass standings!"

@app.route('/jackson')
def birthday():
    return render_template('birthday.html')
