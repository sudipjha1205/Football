import requests
import datetime
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd
import mysql.connector
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



def league_goalie_data(url,lst,table_name):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    for each in comments:
        if 'table' in each:
            try:
                lst.append(pd.read_html(each)[0])
            except:
                continue

    df = lst[0]
    #print(df.columns)
    
    df.columns = df.columns.droplevel(0)
    df = df.fillna(0)

    df.columns = ['Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','Min','90s','GA','GA90','SoTA','Saves','SavePerc','W','D','L','CS','CSperc','PKatt','PKA','PKsv','PKm','SavepercPenalty','Matches']
    df.drop(['Matches'], axis=1, inplace=True)

    df = df[df.Rk != 'Rk']

    df[['Rk','Age','Born','MP','Starts','Min','GA','SoTA','Saves','W','D','L','CS','PKatt','PKA','PKsv','PKm']] = df[['Rk','Age','Born','MP','Starts','Min','GA','SoTA','Saves','W','D','L','CS','PKatt','PKA','PKsv','PKm']].astype('int')
    df[['90s','GA90','SavePerc','CSperc','SavepercPenalty']] = df[['90s','GA90','SavePerc','CSperc','SavepercPenalty']].astype(float)


    connect_mysql(df, table_name)


if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/keepers/Premier-League-Stats','premier_league_goalie']
    la_liga = ["https://fbref.com/en/comps/12/keepers/La-Liga-Stats", 'la_liga_goalie']
    serie_a = ["https://fbref.com/en/comps/11/keepers/Serie-A-Stats", 'serie_a_goalie']
    ligue_1 = ["https://fbref.com/en/comps/13/keepers/Ligue-1-Stats", 'ligue_1_goalie']
    bundesliga = ["https://fbref.com/en/comps/20/keepers/Bundesliga-Stats", 'bundesliga_goalie']

    leagues = [pl,la_liga,serie_a,ligue_1,bundesliga]

    for league in leagues:
        lst = []
        p = Process(target=league_goalie_data, args=(league[0],lst,league[1]))
        p.start()
        p.join()
    
    print(datetime.datetime.now())
    print("DATABASE POPULATED")
    print()
