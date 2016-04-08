import csv

def manager_names():
    names = []
    with open('app/static/rosters.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            names.append(row[0])

    return names

def manager_roster(name):
    with open('app/static/rosters.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == name:
                return row
    
    return ['no_data']