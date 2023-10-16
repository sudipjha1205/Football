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

    df.columns = ['rk', 'player', 'nation', 'pos', 'squad', 'age', 'born', 'ninety_minutes','total_pass_completed','total_pass_attempted','total_pass_completed_perc','total_distance','total_progressive_dist','short_pass_completed','short_pass_attempted','short_pass_completed_perc','medium_pass_completed','medium_pass_attempted','medium_pass_completed_perc','long_pass_completed','long_pass_attempted','long_pass_completed_perc','assists','xag','xa','assistminusxag','key_passes','passes_in_final_third','passes_into_penalty_area','crosses_into_penalty_area','progressive_passes','matches']
    
    df = df[df.rk != 'Rk']
    df.drop(['rk','matches'], axis=1, inplace=True)

    df[['age', 'born','total_pass_completed','total_pass_attempted', 'total_distance','total_progressive_dist','short_pass_completed','short_pass_attempted', 'medium_pass_completed','medium_pass_attempted', 'long_pass_completed','long_pass_attempted', 'assists', 'key_passes','passes_in_final_third','passes_into_penalty_area','crosses_into_penalty_area','progressive_passes']] = df[['age', 'born','total_pass_completed','total_pass_attempted', 'total_distance','total_progressive_dist','short_pass_completed','short_pass_attempted', 'medium_pass_completed','medium_pass_attempted', 'long_pass_completed','long_pass_attempted', 'assists', 'key_passes','passes_in_final_third','passes_into_penalty_area','crosses_into_penalty_area','progressive_passes']].astype('int')

    df[['ninety_minutes', 'total_pass_completed_perc', 'short_pass_completed_perc', 'medium_pass_completed_perc', 'long_pass_completed_perc', 'xag','xa','assistminusxag']] = df[['ninety_minutes', 'total_pass_completed_perc', 'short_pass_completed_perc', 'medium_pass_completed_perc', 'long_pass_completed_perc', 'xag','xa','assistminusxag']].astype(float)

    return df 

if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/passing/Premier-League-Stats','premier_league_passing']
    la_liga = ["https://fbref.com/en/comps/12/passing/La-Liga-Stats", 'la_liga_passing']
    serie_a = ["https://fbref.com/en/comps/11/passing/Serie-A-Stats", 'serie_a_passing']
    ligue_1 = ["https://fbref.com/en/comps/13/passing/Ligue-1-Stats", 'ligue_1_passing']
    bundesliga = ["https://fbref.com/en/comps/20/passing/Bundesliga-Stats", 'bundesliga_passing']

    pl_passing_df = passing_data(pl[0],[],pl[1])
    la_liga_passing_df = passing_data(la_liga[0],[],la_liga[1])
    serie_a_passing_df = passing_data(serie_a[0],[],serie_a[1])
    ligue_1_passing_df = passing_data(ligue_1[0],[],ligue_1[1])
    bundesliga_passing_df = passing_data(bundesliga[0],[],bundesliga[1])

    passing_df = pd.concat([pl_passing_df, la_liga_passing_df, serie_a_passing_df, ligue_1_passing_df, bundesliga_passing_df])
    
    table_name = "passing_data"
    connect_mysql(passing_df,table_name)

    print("DATABASE POPULATED")
