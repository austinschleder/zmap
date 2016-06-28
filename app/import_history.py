import csv

def historic_events():
    with open('app/static/history.csv') as f:
        events = []
        reader = csv.reader(f)
        for row in reader:
            events.append(row)

    return events