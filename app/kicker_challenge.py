from __future__ import print_function
import pandas as pd

def import_kicker_scores():
	kicker_data = pd.read_csv('app/static/kicker_scores.csv')
	return kicker_data

def get_data_overview(kicker_data):
	max_week = max(kicker_data['week'])
	ajs = get_owner_lineup(kicker_data, 'austin')
	ajs_total = sum(ajs['score'])
	ajs_avg = ajs_total/max_week
	tfd = get_owner_lineup(kicker_data, 'thomas')
	tfd_total = sum(tfd['score'])
	tfd_avg = tfd_total/max_week
	differential = ajs_avg - tfd_avg
	points_needed = (17*1.5 - max_week*differential)/(17-max_week)
	data_overview = {
		'max_week':max_week,
		'ajs_avg':ajs_avg,
		'tfd_avg':tfd_avg,
		'differential':differential,
		'points_needed':points_needed
	}
	return data_overview

def get_owner_lineup(kicker_data, owner):
	owner_lineup = kicker_data[kicker_data['owner'] == owner]
	return owner_lineup

if __name__ == '__main__':
	kicker_data = import_kicker_scores()
	print(kicker_data)

	data_overview = get_data_overview(kicker_data)
	print(data_overview)
