from __future__ import print_function
import pandas as pd

def get_q_scores():
	q_scores = pd.read_csv('app/static/q_scores.csv', header=None, names=['team', 'value'])
	return q_scores

def get_hfa():
	hfa = pd.read_csv('app/static/hfa.csv', header=None, names=['team', 'hfa'])
	return hfa