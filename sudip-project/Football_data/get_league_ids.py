import requests
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

querystring = {"season":"2022"}

headers = {
	"X-RapidAPI-Key": "627a6337camsh8c2abad82cd70f7p12c64ajsn4f840c2e3905",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

all_leagues = response.json()
#for i in all_leagues['response']:
#    if i['league']['name'] == 'Premier League' and i['country']['name'] == 'England':
#        print(i)
#        break

df = pd.json_normalize(all_leagues['response'])
print(df)

df2 = df[['league.id','league.name','country.name','country.flag']]
df2.columns = ['id','name','country','flag']

username = "sudip"
password = "Sud1p@jh@"
ip = "localhost:3306"
dbname = "football"

mysql_str = "mysql+mysqlconnector://{}:{}@{}/{}".format(username,password,ip,dbname)
cnx = create_engine(mysql_str)
df2.to_sql(con=cnx, name='league_id', if_exists='replace')

