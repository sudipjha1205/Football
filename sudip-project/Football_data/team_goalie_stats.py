import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
from multiprocessing import Process


def connect_mysql(df,table_name):
    username = "sudip"
    password = "Sud1p@jh@"
    ip = "localhost:3306"
    dbname = "football"

    mysql_str = "mysql+mysqlconnector://{}:{}@{}/{}".format(username,password,ip,dbname)
    cnx = create_engine(mysql_str)
    df.to_sql(con=cnx, name=table_name, if_exists='replace')


def team_attack_stats(url,table_name):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    table1 = soup.find('table', id='stats_squads_keeper_for')

    headers = []
    for i in table1.find_all('th'):
        title = i.text
        headers.append(title)

    
    teams = headers[25:]
    headers = ['Pl', 'MP', 'Starts', 'Min', '90s', 'GA', 'GA90', 'SoTA', 'Saves', 'Saveperc', 'W', 'D', 'L', 'CS', 'CSperc', 'PKatt', 'PKA', 'PKsv', 'PKm', 'Saveperc']
    
    mydata = pd.DataFrame(columns = headers)
    rows = []

    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        rows.append(row)

    rows.pop(0)
    mydata = pd.DataFrame(rows,columns = headers)
    mydata.insert(0,"Squad",teams)

    connect_mysql(mydata,table_name)

if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/keeper/Premier-League-Stats','premier_league_team_keeper']
    la_liga = ["https://fbref.com/en/comps/12/keeper/La-Liga-Stats", 'la_liga_team_keeper']
    serie_a = ["https://fbref.com/en/comps/11/keeper/Serie-A-Stats", 'serie_a_team_keeper']
    ligue_1 = ["https://fbref.com/en/comps/13/keeper/Ligue-1-Stats", 'ligue_1_team_keeper']
    bundesliga = ["https://fbref.com/en/comps/20/keeper/Bundesliga-Stats", 'bundesliga_team_keeper']

    leagues = [pl,la_liga,serie_a,ligue_1,bundesliga]

    for league in leagues:
        p = Process(target=team_attack_stats, args=(league[0],league[1]))
        p.start()
        p.join()

    print("DATABASE POPULATED")


