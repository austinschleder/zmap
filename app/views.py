from flask import render_template
from app import app
import pandas as pd
from app import import_teams, import_scoring, import_updates, import_history, team_data

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title = 'Home')

@app.route('/standings')
def standings():
    latest_date = '2015-06-26'
    full_scores = team_data.full_scores()
    return render_template('standings.html',
                           title = 'Standings',
                           latest_date = latest_date,
                           full_scores = full_scores)

@app.route('/scoring')
def scoring():
    events = import_scoring.scoring_events()
    return render_template('scoring.html',
                           title = 'Scoring',
                           events = events)

@app.route('/managers')
def manager_grid():
    managers = team_data.manager_rosters()
    return render_template('managers.html',
                           title = 'Managers',
                           managers = managers)

@app.route('/draft')
def draft():
    header, teams = import_teams.team_overview()
    return render_template('draft.html',
                           title = 'Draft Prep',
                           header = header,
                           teams = teams)

@app.route('/draft/team_info')
def draft_info():
    header, teams = import_teams.team_overview()
    return render_template('draft_info.html',
                            title = 'Info',
                            header = header,
                            teams = teams)

@app.route('/history')
def history():
    updates = import_history.historic_events()
    updates = updates[1:]
    return render_template('history.html',
                           title = 'History',
                           updates = updates)

@app.route('/updates')
def updates():
    all_updates = import_updates.site_updates()
    reversed_updates = all_updates.reverse()
    latest = all_updates[0]
    others = all_updates[1:]
    return render_template('updates.html',
                           title = 'Updates',
                           latest_update = latest,
                           other_updates = others)

   

