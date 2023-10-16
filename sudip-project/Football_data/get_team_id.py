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

cursor.execute('select id from league_id;')
all_leagues = list(cursor.fetchall())

lst = []
for i in range(len(all_leagues)):
    st = ""
    st = ''.join(map(str,all_leagues[i]))
    lst.append(int(st))

url = "https://api-football-v1.p.rapidapi.com/v3/teams"

headers = {
	"X-RapidAPI-Key": "627a6337camsh8c2abad82cd70f7p12c64ajsn4f840c2e3905",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}


r = []
for i in [39,140,61,135,78]:
    for j in [2022,2023]:
        querystring = {"league":i,"season":j}
        response = requests.get(url, headers=headers, params=querystring)
        response_json = response.json() 
        r.extend(response_json['response'])
        
df = pd.json_normalize(r)
df.columns = ['team_id', 'team_name', 'team_code', 'team_country', 'team_founded','team_national', 'team_logo', 'venue_id', 'venue_name', 'venue_address','venue_city', 'venue_capacity', 'venue_surface', 'venue_image']
print(df)
df.drop_duplicates(subset='team_id',keep='first',inplace=True)


df.to_sql(con=cnx,name='team_id',if_exists='replace')
