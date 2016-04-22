import csv

def current_standings():
    row_num = 0
    latest_date = ''
    owner_standings = ''
    team_standings = []
    with open('app/static/standings.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row_num == 0:
                row_num = 1
                latest_date = row
            else:
                if row_num == 1:
                    row_num = 2
                    owner_standings = row
                else:
                    team_standings.append(row)
    
    return latest_date, owner_standings, team_standings