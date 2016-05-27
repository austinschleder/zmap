import pandas as pd

def raw_team_data():
    df = pd.read_csv('app/static/teams.csv', header=0)

    return df

def manager_scores():
    df = pd.read_csv('app/static/teams.csv', header=0)
    
    x = df.groupby('Manager', as_index=False)['Points'].sum()
    x = x.sort_values(by='Points', ascending=False)
    x = x.values.tolist()

    return x

def manager_rosters():
    x = pd.read_csv('app/static/teams.csv', header=0)
    y = pd.read_csv('app/static/managers.csv', header=0)

    x['Team_Name'] = zip(x.City, x.Nickname)
    x = x.sort_values(by='Round')
    x = x.groupby('Manager', as_index=False).agg({'Team_Name': lambda x: x.tolist()})

    z = pd.merge(y, x, left_on='Manager', right_on='Manager')
    z = z.values.tolist()

    return z

def full_scores():
    df = pd.read_csv('app/static/teams.csv', header=0)
    
    aggregations = {
        'Points': 'sum',
        'Team_Points': lambda x: x.tolist()
    }

    df['Team_Points'] = zip(df.Team, df.Points)
    x = df.sort_values(by='Points', ascending=False)
    x = x.groupby('Manager', as_index=False).agg(aggregations)
    x = x.sort_values(by='Points', ascending=False)
    x = x.values.tolist()

    return x