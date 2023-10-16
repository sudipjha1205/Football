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


def possession_data(url,lst,table_name):
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

    df.columns = ['rk', 'player', 'nation', 'pos', 'squad', 'age', 'born', 'ninety_minutes','touches','touches_in_def_penalty_area','touches_in_def_3rd','touches_in_mid_3rd','touches_in_att_3rd','touches_in_att_penalty_area','live_ball_touches','take_ons_attempted','take_ons_succeeded','take_ons_success_perc','tackled_during_take_on','perc_time_tackled_during_take_on','carries','total_carry_dist','progressive_dist','progressive_carries','carries_in_final_3rd','carries_in_penalty_area','miscontrols','dispossessed','passess_received','progressive_passess_received','matches']
    
    df = df[df.rk != 'Rk']
    df.drop(['rk','matches'], axis=1, inplace=True)

    df[['age', 'born','touches','touches_in_def_penalty_area','touches_in_def_3rd','touches_in_mid_3rd','touches_in_att_3rd','touches_in_att_penalty_area','live_ball_touches','take_ons_attempted','take_ons_succeeded','tackled_during_take_on','carries','total_carry_dist','progressive_dist','progressive_carries','carries_in_final_3rd','carries_in_penalty_area','miscontrols','dispossessed','passess_received','progressive_passess_received']] = df[['age', 'born','touches','touches_in_def_penalty_area','touches_in_def_3rd','touches_in_mid_3rd','touches_in_att_3rd','touches_in_att_penalty_area','live_ball_touches','take_ons_attempted','take_ons_succeeded','tackled_during_take_on','carries','total_carry_dist','progressive_dist','progressive_carries','carries_in_final_3rd','carries_in_penalty_area','miscontrols','dispossessed','passess_received','progressive_passess_received']].astype('int')

    df[['ninety_minutes', 'take_ons_success_perc', 'perc_time_tackled_during_take_on']] = df[['ninety_minutes', 'take_ons_success_perc', 'perc_time_tackled_during_take_on']].astype(float)

    return df 

if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/possession/Premier-League-Stats','premier_league_possession']
    la_liga = ["https://fbref.com/en/comps/12/possession/La-Liga-Stats", 'la_liga_possession']
    serie_a = ["https://fbref.com/en/comps/11/possession/Serie-A-Stats", 'serie_a_possession']
    ligue_1 = ["https://fbref.com/en/comps/13/possession/Ligue-1-Stats", 'ligue_1_possession']
    bundesliga = ["https://fbref.com/en/comps/20/possession/Bundesliga-Stats", 'bundesliga_possession']

    pl_possession_df = possession_data(pl[0],[],pl[1])
    la_liga_possession_df = possession_data(la_liga[0],[],la_liga[1])
    serie_a_possession_df = possession_data(serie_a[0],[],serie_a[1])
    ligue_1_possession_df = possession_data(ligue_1[0],[],ligue_1[1])
    bundesliga_possession_df = possession_data(bundesliga[0],[],bundesliga[1])

    possession_df = pd.concat([pl_possession_df, la_liga_possession_df, serie_a_possession_df, ligue_1_possession_df, bundesliga_possession_df])
    
    table_name = "possession_data"
    connect_mysql(possession_df,table_name)

    print("DATABASE POPULATED")
