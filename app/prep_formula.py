from __future__ import print_function
import nfldb
import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
from pandas.stats.api import ols
import scipy
import sys

db = nfldb.connect()

def get_game_scores(season, max_week=17):
	q = nfldb.Query(db)
	q.game(season_year=season, season_type='Regular', week=range(max_week))
	weeks = q.sort(('gsis_id', 'asc')).as_games()
	week_data = [[w.home_team, w.away_team, w.home_score - w.away_score] for w in weeks]
	scores = pd.DataFrame(week_data, columns=['home_team', 'away_team', 'point_diff'])
	scores.to_csv('app/static/{}_game_scores.csv'.format(season), index=False)
	return scores

def get_all_teams(season):
	q = nfldb.Query(db)
	q.game(season_year=season, season_type='Regular')
	weeks = q.sort(('gsis_id', 'asc')).as_games()
	home_teams = [w.home_team for w in weeks]
	away_teams = [w.away_team for w in weeks]
	all_teams = sorted(list(set(home_teams + away_teams)))
	return all_teams

def create_formula_matrix(scores, all_teams):
	point_diffs = scores['point_diff']
	formula_matrix = pd.DataFrame(columns=all_teams)
	for team in all_teams:
		formula_matrix[team] = np.where(scores['home_team'] == team, 1, np.where(scores['away_team'] == team, -1, 0))
	res = ols(y=point_diffs, x=formula_matrix.drop(['ARI'], axis=1))
	q_scores = res.beta[0:-1]
	q_scores['ARI'] = 0
	q_scores -= min(res.beta)
	q_scores.sort_values(ascending=False, inplace=True)
	q_scores.to_csv('app/static/q_scores.csv', float_format='%.2f')
	hfa = pd.Series(res.beta['intercept'])
	hfa.to_csv('app/static/hfa.csv')

if __name__ == '__main__':
	prediction_week = int(sys.argv[1]) if len(sys.argv) > 1 else 17
	season = int(sys.argv[2]) if len(sys.argv) > 2 else 2016
	scores = get_game_scores(season, prediction_week)
	all_teams = get_all_teams(season)
	create_formula_matrix(scores, all_teams)