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


def team_defense_stats(url,table_name):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    table1 = soup.find('table', id='stats_squads_defense_for')

    headers = []
    for i in table1.find_all('th'):
        title = i.text
        headers.append(title)

    print(headers)
''' 
    teams = headers[24:]
    headers = ['Pl', '90s', 'Tkl', 'TklW', 'Def_3rd', 'Mid_3rd', 'Att_3rd', 'Tkl', 'Att', 'Tklperc', 'Lost', 'Blocks', 'Sh', 'Pass', 'Int', 'TklInt', 'Clr', 'Err']
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
    pl = ['https://fbref.com/en/comps/9/defense/Premier-League-Stats','premier_league_team_defense']
    la_liga = ["https://fbref.com/en/comps/12/defense/La-Liga-Stats", 'la_liga_team_defense']
    serie_a = ["https://fbref.com/en/comps/11/defense/Serie-A-Stats", 'serie_a_team_defense']
    ligue_1 = ["https://fbref.com/en/comps/13/defense/Ligue-1-Stats", 'ligue_1_team_defense']
    bundesliga = ["https://fbref.com/en/comps/20/defense/Bundesliga-Stats", 'bundesliga_team_defense']
                "https://fbref.com/en/comps/20/passing/Bundesliga-Stats"
    leagues = [pl,la_liga,serie_a,ligue_1,bundesliga]

    for league in leagues:
        p = Process(target=team_defense_stats, args=(league[0],league[1]))
        p.start()
        p.join()

    print("DATABASE POPULATED")

'''

team_defense_stats('https://fbref.com/en/comps/20/passing/Bundesliga-Stats','xyz')
