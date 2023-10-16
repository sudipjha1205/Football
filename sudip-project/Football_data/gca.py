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


def gca_data(url,lst,table_name):
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

    df.columns = ['rk', 'player', 'nation', 'pos', 'squad', 'age', 'born', 'ninety_minutes','sca','scaperninety','live_pass_sca','dead_pass_sca','take_on_sca','shot_sca','fouls_sca','def_action_sca','gca','gcaperninety','live_pass_gca','dead_pass_gca','take_on_gca','shot_gca','fouls_gca','def_action_gca','matches']
    
    df = df[df.rk != 'Rk']
    df.drop(['rk','matches'], axis=1, inplace=True)

    df[['age', 'born','sca','live_pass_sca','dead_pass_sca','take_on_sca','shot_sca','fouls_sca','def_action_sca','gca','live_pass_gca','dead_pass_gca','take_on_gca','shot_gca','fouls_gca','def_action_gca']] = df[['age', 'born', 'sca', 'live_pass_sca','dead_pass_sca','take_on_sca','shot_sca','fouls_sca','def_action_sca','gca','live_pass_gca','dead_pass_gca','take_on_gca','shot_gca','fouls_gca','def_action_gca']].astype('int')

    df[['ninety_minutes', 'scaperninety', 'gcaperninety']] = df[['ninety_minutes', 'scaperninety', 'gcaperninety' ]].astype(float)

    return df 

if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/gca/Premier-League-Stats','premier_league_gca']
    la_liga = ["https://fbref.com/en/comps/12/gca/La-Liga-Stats", 'la_liga_gca']
    serie_a = ["https://fbref.com/en/comps/11/gca/Serie-A-Stats", 'serie_a_gca']
    ligue_1 = ["https://fbref.com/en/comps/13/gca/Ligue-1-Stats", 'ligue_1_gca']
    bundesliga = ["https://fbref.com/en/comps/20/gca/Bundesliga-Stats", 'bundesliga_gca']

    pl_gca_df = gca_data(pl[0],[],pl[1])
    la_liga_gca_df = gca_data(la_liga[0],[],la_liga[1])
    serie_a_gca_df = gca_data(serie_a[0],[],serie_a[1])
    ligue_1_gca_df = gca_data(ligue_1[0],[],ligue_1[1])
    bundesliga_gca_df = gca_data(bundesliga[0],[],bundesliga[1])

    gca_df = pd.concat([pl_gca_df, la_liga_gca_df, serie_a_gca_df, ligue_1_gca_df, bundesliga_gca_df])
    
    table_name = "gca_data"
    connect_mysql(gca_df,table_name)

    print("DATABASE POPULATED")
