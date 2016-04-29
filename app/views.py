from flask import render_template
from app import app, import_teams, import_managers, import_scoring, import_rosters, import_standings

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title = 'Home')

@app.route('/standings')
def standings():
    latest_date, owner_standings, team_standings = import_standings.current_standings()
    return render_template('standings.html',
                           title = 'Standings',
                           latest_date = latest_date,
                           owner_standings = owner_standings,
                           team_standings = team_standings)

@app.route('/scoring')
def scoring():
    events = import_scoring.scoring_events()
    return render_template('scoring.html',
                           title = 'Scoring',
                           events = events)

@app.route('/managers')
def managers():
    manager_names = import_managers.manager_names()
    manager_names = manager_names[1:]
    return render_template('managers.html',
                           title = 'Managers',
                           manager_names = manager_names)

@app.route('/managers/<manager_name>')
def manager(manager_name):
    manager_data = import_managers.manager_data(manager_name)
    manager_teams = import_rosters.manager_roster(manager_name)
    return render_template('manager.html',
                           title = manager_name,
                           data = manager_data,
                           teams = manager_teams)

@app.route('/draft')
def draft():
    header, teams = import_teams.team_overview()
    return render_template('draft.html',
                           title = 'Draft Prep',
                           header = header,
                           teams = teams)

@app.route('/updates')
def updates():
    return render_template('updates.html',
                           title = 'Updates')

   

