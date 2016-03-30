from flask import render_template
from app import app, import_teams, import_managers, import_scoring

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title = 'Home')

@app.route('/scoring')
def scoring():
    events = import_scoring.scoring_events()
    return render_template('scoring.html',
                           title = 'Scoring',
                           events = events)

@app.route('/draft')
def draft():
    header, teams = import_teams.team_overview()
    return render_template('draft.html',
                           title = 'Draft Prep',
                           header = header,
                           teams = teams)

@app.route('/managers')
def managers():
    manager_names = import_managers.manager_names()
    manager_names = manager_names[1:]
    return render_template('managers.html',
                           title = 'Managers',
                           manager_names = manager_names)

@app.route('/standings')
def standings():
    return "Under construction! Stay tuned for some kick-ass standings!"

@app.route('/updates')
def updates():
    return render_template('updates.html',
                           title = 'Updates')

@app.route('/managers/austin')
def manager_austin():
    manager_data = import_managers.manager_data('austin')
    return render_template('manager.html',
                           title = manager_data[1],
                           data = manager_data)

@app.route('/managers/max')
def manager_max():
    manager_data = import_managers.manager_data('max')
    return render_template('manager.html',
                           title = manager_data[1],
                           data = manager_data)

@app.route('/managers/zack')
def manager_zack():
    manager_data = import_managers.manager_data('zack')
    return render_template('manager.html',
                           title = manager_data[1],
                           data = manager_data)

@app.route('/managers/patrick')
def manager_patrick():
    manager_data = import_managers.manager_data('patrick')
    return render_template('manager.html',
                           title = manager_data[1],
                           data = manager_data)

@app.route('/managers/matt')
def manager_matt():
    manager_data = import_managers.manager_data('matt')
    return render_template('manager.html',
                           title = manager_data[1],
                           data = manager_data)

@app.route('/managers/chris')
def manager_chris():
    manager_data = import_managers.manager_data('chris')
    return render_template('manager.html',
                           title = manager_data[1],
                           data = manager_data)


@app.route('/dominos')
def dominos():
    return "Yeah, OK. Domino's is cool with me."



