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



def league_defender_data(url,lst,table_name):
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

    df.columns = ['Rk','Player','Nation','Pos','Squad','Age','Born','90s','Tkl','TklW','Def_3rd','Mid_3rd','Att_3rd','Tkl_Drib','Att_Drib','Tkl_Per','Lost','Blocks','shot','Pass','Int','IntplusTkl','Clr','Err','Matches']
    df.drop(['Matches'], axis=1, inplace=True)

    df = df[df.Rk != 'Rk']

    df[['Rk','Age', 'Born', 'Tkl','TklW','Def_3rd','Mid_3rd','Att_3rd','Tkl_Drib','Att_Drib','Lost','Blocks','shot','Pass','Int','IntplusTkl','Clr','Err']] = df[['Rk','Age', 'Born', 'Tkl','TklW','Def_3rd','Mid_3rd','Att_3rd','Tkl_Drib','Att_Drib','Lost','Blocks','shot','Pass','Int','IntplusTkl','Clr','Err']].astype('int')
    df[['90s',  'Tkl_Per']] = df[['90s', 'Tkl_Per']].astype(float)


    connect_mysql(df, table_name)


if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/defense/Premier-League-Stats','premier_league_defenders']
    la_liga = ["https://fbref.com/en/comps/12/defense/La-Liga-Stats", 'la_liga_defenders']
    serie_a = ["https://fbref.com/en/comps/11/defense/Serie-A-Stats", 'serie_a_defenders']
    ligue_1 = ["https://fbref.com/en/comps/13/defense/Ligue-1-Stats", 'ligue_1_defenders']
    bundesliga = ["https://fbref.com/en/comps/20/defense/Bundesliga-Stats", 'bundesliga_defenders']

    leagues = [pl,la_liga,serie_a,ligue_1,bundesliga]

    for league in leagues:
        lst = []
        p = Process(target=league_defender_data, args=(league[0],lst,league[1]))
        p.start()
        p.join()

    print("DATABASE POPULATED")
