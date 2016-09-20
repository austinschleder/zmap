from __future__ import print_function
import nfldb
import pandas as pd

db = nfldb.connect()

def read_in_kicker_selections(file):
	selections = pd.read_csv(file)
	selections['score'] = selections.apply(lambda x: get_kicker_score(x['kicker'], x['week']), axis=1)
	return selections

def get_kicker_score(kicker_name, week):
	q = nfldb.Query(db)
	CURRENT_SEASON = 2016
	q.game(season_year=CURRENT_SEASON, season_type='Regular', week=week)
	q.player(full_name=kicker_name)
	game_points = sum([get_play_score(p) for p in q.as_plays()])
	return game_points

def get_play_score(play):
	play_points = 0.0
	if play.kicking_fga:
		play_points = max(play.kicking_fgm_yds/10, 3*play.kicking_fgm) - (1.0 * play.kicking_fgmissed)
	elif play.kicking_xpa:
		play_points = 1.0 * play.kicking_xpmade - 1.0 * play.kicking_xpmissed
	return play_points

if __name__ == '__main__':
	selections = read_in_kicker_selections('app/static/kicker_selections.csv')
	selections.to_csv('app/static/kicker_scores.csv', index=False)

	print(selections)