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
    df.columns = df.columns.droplevel(0)
    df = df.fillna(0)

    df.columns = ['Rk','Player','Nation','Pos','Squad','Age','Born','90s','GA','PKA','FK','CK','OG','PSxg','PSxgvsSot','PSxgminusGA','PSxgminusGAper90','LCMp','LAtt','LCmpperc','PAtt','PThr','PLaunedperc','PAvgLen','GKAtt','GKLaunchPerc','GKAvgLen','CrossessFaced','CrossedStopped','StopPrecentage','DefActOutPenalBox','DefActOutPenalBoxPer90','AverageDistfromPenalBox','Matches']
    df.drop(['Matches'], axis=1, inplace=True)

    df = df[df.Rk != 'Rk']

    df[['Rk','Age', 'Born','GA','PKA','FK','CK','OG','LCMp','LAtt','PAtt','PThr','GKAtt','CrossessFaced','CrossedStopped','DefActOutPenalBox']] = df[['Rk','Age', 'Born','GA','PKA','FK','CK','OG','LCMp','LAtt','PAtt','PThr','GKAtt','CrossessFaced','CrossedStopped','DefActOutPenalBox']].astype('int')
    df[['90s','PSxg','PSxgvsSot','PSxgminusGA','PSxgminusGAper90','LCmpperc','PLaunedperc','PAvgLen','GKLaunchPerc','GKAvgLen','StopPrecentage','DefActOutPenalBoxPer90','AverageDistfromPenalBox']] = df[['90s','PSxg','PSxgvsSot','PSxgminusGA','PSxgminusGAper90','LCmpperc','PLaunedperc','PAvgLen','GKLaunchPerc','GKAvgLen','StopPrecentage','DefActOutPenalBoxPer90','AverageDistfromPenalBox' ]].astype(float)


    connect_mysql(df, table_name)


if __name__ == "__main__":
    pl = ['https://fbref.com/en/comps/9/keepersadv/Premier-League-Stats','premier_league_goalie_adv']
    la_liga = ["https://fbref.com/en/comps/12/keepersadv/La-Liga-Stats", 'la_liga_goalie_adv']
    serie_a = ["https://fbref.com/en/comps/11/keepersadv/Serie-A-Stats", 'serie_a_goalie_adv']
    ligue_1 = ["https://fbref.com/en/comps/13/keepersadv/Ligue-1-Stats", 'ligue_1_goalie_adv']
    bundesliga = ["https://fbref.com/en/comps/20/keepersadv/Bundesliga-Stats", 'bundesliga_goalie_adv']

    leagues = [pl,la_liga,serie_a,ligue_1,bundesliga]

    for league in leagues:
        lst = []
        p = Process(target=league_goalie_data, args=(league[0],lst,league[1]))
        p.start()
        p.join()

    print("DATABASE POPULATED")
