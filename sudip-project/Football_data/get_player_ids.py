import time
import requests
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

username = "sudip"
password = "Sud1p@jh@"
ip = "localhost:3306"
dbname = "football"

mysql_str = "mysql+mysqlconnector://{}:{}@{}/{}".format(username,password,ip,dbname)
cnx = create_engine(mysql_str)
connection = cnx.raw_connection()
cursor = connection.cursor()

cursor.execute('select team_id from team_id;')
all_leagues = list(cursor.fetchall())

lst = []
for i in range(len(all_leagues)):
    st = ""
    st = ''.join(map(str,all_leagues[i]))
    lst.append(int(st))


players_data_list = []
def call_api(endpoint, params={}):
    base_url = 'https://api-football-v1.p.rapidapi.com/v3/'
    headers = {
            "X-RapidAPI-Key": "627a6337camsh8c2abad82cd70f7p12c64ajsn4f840c2e3905",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }


    response = requests.get(base_url + endpoint, params=params, headers=headers)
    response_data = response.json()
    return response_data

def players_data(league, season, page=1, players_data_list=[]):
    params = {
        'league': league,
        'season': season,
        'page': page
    }
    
    players = call_api('players', params)
    players_data_list.append(players)
    
    try:
        if players['paging']['current'] < players['paging']['total']:
            page = players['paging']['current'] + 1
            if page % 2 == 1:
                time.sleep(1)
            players_data_list = players_data(league, season, page, players_data_list)
    except:
        pass

    return players_data_list

# Get all the teams from this competition
teams = call_api('teams', {'league': 39, 'season': 2022})
#print(teams)  # To display the results if necessary

# Get all the players from this competition
players = players_data(39, 2022)
#print(players)  # To display the results if necessary

print(players[-1])

df = pd.json_normalize(players)
df2 = pd.json_normalize(df['statistics'][0])
#print(df.head(1).values.tolist()[0])
print(df[df['player.name'].str.contains('Haaland')].values.tolist())

