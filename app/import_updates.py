import csv

def site_updates():
    with open('app/static/site_updates.csv') as f:
        updates = []
        reader = csv.reader(f)
        for row in reader:
            updates.append(row)

    return updates