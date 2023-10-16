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


def misc_data(url,lst,table_name):
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

    df.columns = ['rk', 'player', 'nation', 'pos', 'squad', 'age', 'born', 'ninety_minutes','yellow_card','red_card','second_yellow_card','fouls_committed','fouls_drawn','offsides','crosses','interception','tackle_won','penalty_won','penalty_conceded','own_goals','recoveries','aerial_duels_won','aerial_duels_lost','aerial_duels_won_perc','matches']
    
    df = df[df.rk != 'Rk']
    df.drop(['rk','matches'], axis=1, inplace=True)

    df[['age', 'born','yellow_card','red_card','second_yellow_card','fouls_committed','fouls_drawn','offsides','crosses','interception','tackle_won','penalty_won','penalty_conceded','own_goals','recoveries','aerial_duels_won','aerial_duels_lost']] = df[['age', 'born','yellow_card','red_card','second_yellow_card','fouls_committed','fouls_drawn','offsides','crosses','interception','tackle_won','penalty_won','penalty_conceded','own_goals','recoveries','aerial_duels_won','aerial_duels_lost']].astype('int')

    df[['ninety_minutes', 'aerial_duels_won_perc']] = df[['ninety_minutes', 'aerial_duels_won_perc']].astype(float)

    return df 

if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/misc/Premier-League-Stats','premier_league_misc']
    la_liga = ["https://fbref.com/en/comps/12/misc/La-Liga-Stats", 'la_liga_misc']
    serie_a = ["https://fbref.com/en/comps/11/misc/Serie-A-Stats", 'serie_a_misc']
    ligue_1 = ["https://fbref.com/en/comps/13/misc/Ligue-1-Stats", 'ligue_1_misc']
    bundesliga = ["https://fbref.com/en/comps/20/misc/Bundesliga-Stats", 'bundesliga_misc']

    pl_misc_df = misc_data(pl[0],[],pl[1])
    la_liga_misc_df = misc_data(la_liga[0],[],la_liga[1])
    serie_a_misc_df = misc_data(serie_a[0],[],serie_a[1])
    ligue_1_misc_df = misc_data(ligue_1[0],[],ligue_1[1])
    bundesliga_misc_df = misc_data(bundesliga[0],[],bundesliga[1])

    misc_df = pd.concat([pl_misc_df, la_liga_misc_df, serie_a_misc_df, ligue_1_misc_df, bundesliga_misc_df])
    
    table_name = "misc_data"
    connect_mysql(misc_df,table_name)

    print("DATABASE POPULATED")
