import requests
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



def league_attacker_data(url,lst,table_name):
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
    df.columns = df.columns.droplevel(0)
    df = df.fillna(0)

    df.columns = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Age', 'Born', 'MP', 'Starts', 'Min', '90s', 'Gls', 'Ast', 'GA', 'GminusPK', 'PK', 'PKatt', 'CrdY', 'CrdR', 'xG', 'npxG', 'xAG', 'npxGxAG', 'PrgC', 'PrgP', 'PrgR', 'Glsp90', 'Astp90', 'GAp90', 'GminusPKp90', 'GAminusPKp90', 'xGp90', 'xAGp90', 'xGxAGp90', 'npxGp90', 'npxGxAGp90', 'Matches']
    df.drop(['Matches'], axis=1, inplace=True)

    df = df[df.Rk != 'Rk']

    df[['Rk','Age', 'Born', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'GA', 'GminusPK', 'PK', 'PKatt', 'CrdY', 'CrdR', 'PrgC', 'PrgP', 'PrgR']] = df[['Rk','Age', 'Born', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'GA', 'GminusPK', 'PK', 'PKatt', 'CrdY', 'CrdR', 'PrgC', 'PrgP', 'PrgR']].astype('int')
    df[['90s', 'xG', 'npxG', 'xAG', 'npxG+xAG',  'Glsp90', 'Astp90', 'GAp90', 'GminusPKp90', 'GAminusPKp90', 'xGp90', 'xAGp90', 'xGxAGp90', 'npxGp90', 'npxGxAGp90']] = df[['90s', 'xG', 'npxG', 'xAG', 'npxGxAG',  'Glsp90', 'Astp90', 'GAp90', 'GminusPKp90', 'GAminusPKp90', 'xGp90', 'xAGp90', 'xGxAGp90', 'npxGp90', 'npxGxAGp90']].astype(float)


    connect_mysql(df, table_name)


if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/stats/Premier-League-Stats','premier_league_attackers']
    la_liga = ["https://fbref.com/en/comps/12/stats/La-Liga-Stats", 'la_liga_attackers']
    serie_a = ["https://fbref.com/en/comps/11/stats/Serie-A-Stats", 'serie_a_attackers']
    ligue_1 = ["https://fbref.com/en/comps/13/stats/Ligue-1-Stats", 'ligue_1_attackers']
    bundesliga = ["https://fbref.com/en/comps/20/stats/Bundesliga-Stats", 'bundesliga_attackers']

    leagues = [pl,la_liga,serie_a,ligue_1,bundesliga]

    for league in leagues:
        lst = []
        p = Process(target=league_attacker_data, args=(league[0],lst,league[1]))
        p.start()
        p.join()

    print("DATABASE POPULATED")
