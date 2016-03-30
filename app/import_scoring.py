import csv

def scoring_events():
    with open('app/static/scoring_events.csv') as f:
        events = []
        reader = csv.reader(f)
        for row in reader:
            events.append(row)

    return events
