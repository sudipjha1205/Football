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


def passing_data(url,lst,table_name):
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

    df.columns = ['rk', 'player', 'nation', 'pos', 'squad', 'age', 'born', 'ninety_minutes','total_pass_attempted','live_pass','dead_pass','free_kick','through_balls','switches','crosses','throw_ins','corner_kicks','corner_ins','corner_out','straight_corner','passess_completed','offside_passess','passess_blocked','matches']
    
    df = df[df.rk != 'Rk']
    df.drop(['rk','matches'], axis=1, inplace=True)

    df[['age', 'born', 'total_pass_attempted','live_pass','dead_pass','free_kick','through_balls','switches','crosses','throw_ins','corner_kicks','corner_ins','corner_out','straight_corner','passess_completed','offside_passess','passess_blocked']] = df[['age', 'born', 'total_pass_attempted','live_pass','dead_pass','free_kick','through_balls','switches','crosses','throw_ins','corner_kicks','corner_ins','corner_out','straight_corner','passess_completed','offside_passess','passess_blocked']].astype('int')

    df[['ninety_minutes']] = df[['ninety_minutes']].astype(float)

    return df 

if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/passing_types/Premier-League-Stats','premier_league_passing_types']
    la_liga = ["https://fbref.com/en/comps/12/passing_types/La-Liga-Stats", 'la_liga_passing_types']
    serie_a = ["https://fbref.com/en/comps/11/passing_types/Serie-A-Stats", 'serie_a_passing_types']
    ligue_1 = ["https://fbref.com/en/comps/13/passing_types/Ligue-1-Stats", 'ligue_1_passing_types']
    bundesliga = ["https://fbref.com/en/comps/20/passing_types/Bundesliga-Stats", 'bundesliga_passing_types']

    pl_passing_df = passing_data(pl[0],[],pl[1])
    la_liga_passing_df = passing_data(la_liga[0],[],la_liga[1])
    serie_a_passing_df = passing_data(serie_a[0],[],serie_a[1])
    ligue_1_passing_df = passing_data(ligue_1[0],[],ligue_1[1])
    bundesliga_passing_df = passing_data(bundesliga[0],[],bundesliga[1])

    passing_df = pd.concat([pl_passing_df, la_liga_passing_df, serie_a_passing_df, ligue_1_passing_df, bundesliga_passing_df])
    
    table_name = "pass_type_data"
    connect_mysql(passing_df,table_name)

    print("DATABASE POPULATED")
