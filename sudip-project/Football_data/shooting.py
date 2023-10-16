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

    cnx.execute("ALTER TABLE {} ADD id integer AUTO_INCREMENT NOT NULL PRIMARY KEY FIRST;".format(table_name))


def shooting_data(url,lst,table_name):
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

    df.columns = ['rk', 'player', 'nation', 'pos', 'squad', 'age', 'born', 'ninety_minutes', 'gls', 'total_shot', 'total_shot_on_target','shot_on_target_perc','shot_on_target_per90','shot_on_target_per90','goal_per_shot','goal_per_shot_on_target','avg_shot_distance','shots_from_free_kick','penalty_kick','penalty_kick_attempted','xg','npxg','npxgpershot','goalminusxg','npgoalminusxg','matches']
    
    df = df[df.rk != 'Rk']
    df.drop(['rk','matches'], axis=1, inplace=True)

    df[['age', 'born','gls', 'total_shot', 'total_shot_on_target', 'shots_from_free_kick','penalty_kick','penalty_kick_attempted']] = df[['age', 'born','gls', 'total_shot', 'total_shot_on_target', 'shots_from_free_kick','penalty_kick','penalty_kick_attempted']].astype('int')

    #df[['ninety_minutes', 'shot_on_target_perc','shot_on_target_per90','shot_on_target_per90','goal_per_shot','goal_per_shot_on_target','avg_shot_distance', 'xg','npxg','npxgpershot','goalminusxg','npgoalminusxg']] = df[['ninety_minutes', 'shot_on_target_perc','shot_on_target_per90','shot_on_target_per90','goal_per_shot','goal_per_shot_on_target','avg_shot_distance', 'xg','npxg','npxgpershot','goalminusxg','npgoalminusxg']].astype(float)

    return df 

if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/shooting/Premier-League-Stats','premier_league_shooting']
    la_liga = ["https://fbref.com/en/comps/12/shooting/La-Liga-Stats", 'la_liga_shooting']
    serie_a = ["https://fbref.com/en/comps/11/shooting/Serie-A-Stats", 'serie_a_shooting']
    ligue_1 = ["https://fbref.com/en/comps/13/shooting/Ligue-1-Stats", 'ligue_1_shooting']
    bundesliga = ["https://fbref.com/en/comps/20/shooting/Bundesliga-Stats", 'bundesliga_shooting']

    pl_shooting_df = shooting_data(pl[0],[],pl[1])
    la_liga_shooting_df = shooting_data(la_liga[0],[],la_liga[1])
    serie_a_shooting_df = shooting_data(serie_a[0],[],serie_a[1])
    ligue_1_shooting_df = shooting_data(ligue_1[0],[],ligue_1[1])
    bundesliga_shooting_df = shooting_data(bundesliga[0],[],bundesliga[1])

    shooting_df = pd.concat([pl_shooting_df, la_liga_shooting_df, serie_a_shooting_df, ligue_1_shooting_df, bundesliga_shooting_df])
    
    table_name = "shooting_data"
    connect_mysql(shooting_df,table_name)

    print("DATABASE POPULATED")
