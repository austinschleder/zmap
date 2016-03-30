import csv

def team_overview():
    teams = []
    rownum = 0
    header = ''
    with open('app/static/team_overview.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if rownum == 0:
                header = row
                rownum += 1
            else:
                teams.append(row)
    
    return header, teams
