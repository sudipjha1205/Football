import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd
from sqlalchemy import create_engine

def connect_mysql():
    username = "sudip"
    password = "Sud1p@jh@"
    ip = "localhost:3306"
    dbname = "football"

    mysql_str = "mysql+mysqlconnector://{}:{}@{}/{}".format(username,password,ip,dbname)
    cnx = create_engine(mysql_str)

    return cnx

conn = connect_mysql()

def consolidated_attacker_data():
    with conn.connect() as connection:
        pl_data = connection.execute("SELECT * FROM premier_league_attackers;").fetchall()
        pl_df = pd.DataFrame(pl_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','Min','90s','Gls','Ast','GA','GminusPK','PK','PKatt','CrdY','CrdR','xG','npxG','xAG','npxGxAG','PrgC','PrgP','PrgR','Glsp90','Astp90','GAp90','GminusPKp90','GAminusPKp90','xGp90','xAGp90','xGxAGp90','npxGp90','npxGxAGp90', 'npxGxAG'])
        pl_df.drop(['index','Rk'],axis=1,inplace=True)


        la_liga_data = connection.execute("SELECT * FROM la_liga_attackers;").fetchall()
        la_liga_df = pd.DataFrame(la_liga_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','Min','90s','Gls','Ast','GA','GminusPK','PK','PKatt','CrdY','CrdR','xG','npxG','xAG','npxGxAG','PrgC','PrgP','PrgR','Glsp90','Astp90','GAp90','GminusPKp90','GAminusPKp90','xGp90','xAGp90','xGxAGp90','npxGp90','npxGxAGp90', 'npxGxAG'])
        la_liga_df.drop(['index','Rk'],axis=1,inplace=True)


        bundesliga_data = connection.execute("SELECT * FROM bundesliga_attackers;").fetchall()
        bundesliga_df = pd.DataFrame(bundesliga_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','Min','90s','Gls','Ast','GA','GminusPK','PK','PKatt','CrdY','CrdR','xG','npxG','xAG','npxGxAG','PrgC','PrgP','PrgR','Glsp90','Astp90','GAp90','GminusPKp90','GAminusPKp90','xGp90','xAGp90','xGxAGp90','npxGp90','npxGxAGp90', 'npxGxAG'])
        bundesliga_df.drop(['index','Rk'],axis=1,inplace=True)


        ligue_1_data = connection.execute("SELECT * FROM ligue_1_attackers;").fetchall()
        ligue_1_df = pd.DataFrame(ligue_1_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','Min','90s','Gls','Ast','GA','GminusPK','PK','PKatt','CrdY','CrdR','xG','npxG','xAG','npxGxAG','PrgC','PrgP','PrgR','Glsp90','Astp90','GAp90','GminusPKp90','GAminusPKp90','xGp90','xAGp90','xGxAGp90','npxGp90','npxGxAGp90', 'npxGxAG'])
        ligue_1_df.drop(['index','Rk'],axis=1,inplace=True)


        serie_a_data = connection.execute("SELECT * FROM serie_a_attackers;").fetchall()
        serie_a_df = pd.DataFrame(serie_a_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','Min','90s','Gls','Ast','GA','GminusPK','PK','PKatt','CrdY','CrdR','xG','npxG','xAG','npxGxAG','PrgC','PrgP','PrgR','Glsp90','Astp90','GAp90','GminusPKp90','GAminusPKp90','xGp90','xAGp90','xGxAGp90','npxGp90','npxGxAGp90', 'npxGxAG'])
        serie_a_df.drop(['index','Rk'],axis=1,inplace=True)


        dfs = [pl_df,la_liga_df,bundesliga_df,ligue_1_df,serie_a_df]
        df = pd.concat(dfs)

        return df

def consolidated_defender_data():
    with conn.connect() as connection:
        pl_data = connection.execute("SELECT * FROM premier_league_defenders;").fetchall()
        pl_df = pd.DataFrame(pl_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','90s','Tkl','TklW','Def_3rd','Mid_3rd','Att_3rd','Tkl_Drib','Att_Drib','Tkl_Per','Lost','Blocks','shot','Pass','Int','IntplusTkl','Clr','Err'])


        la_liga_data = connection.execute("SELECT * FROM la_liga_defenders;").fetchall()
        la_liga_df = pd.DataFrame(la_liga_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','90s','Tkl','TklW','Def_3rd','Mid_3rd','Att_3rd','Tkl_Drib','Att_Drib','Tkl_Per','Lost','Blocks','shot','Pass','Int','IntplusTkl','Clr','Err'])


        bundesliga_data = connection.execute("SELECT * FROM bundesliga_defenders;").fetchall()
        bundesliga_df = pd.DataFrame(bundesliga_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','90s','Tkl','TklW','Def_3rd','Mid_3rd','Att_3rd','Tkl_Drib','Att_Drib','Tkl_Per','Lost','Blocks','shot','Pass','Int','IntplusTkl','Clr','Err'])


        ligue_1_data = connection.execute("SELECT * FROM ligue_1_defenders;").fetchall()
        ligue_1_df = pd.DataFrame(ligue_1_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','90s','Tkl','TklW','Def_3rd','Mid_3rd','Att_3rd','Tkl_Drib','Att_Drib','Tkl_Per','Lost','Blocks','shot','Pass','Int','IntplusTkl','Clr','Err'])


        serie_a_data = connection.execute("SELECT * FROM serie_a_defenders;").fetchall()
        serie_a_df = pd.DataFrame(serie_a_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','90s','Tkl','TklW','Def_3rd','Mid_3rd','Att_3rd','Tkl_Drib','Att_Drib','Tkl_Per','Lost','Blocks','shot','Pass','Int','IntplusTkl','Clr','Err'])


        dfs = [pl_df,la_liga_df,bundesliga_df,ligue_1_df,serie_a_df]
        df = pd.concat(dfs)
        df.drop(['index','Rk'],axis=1,inplace=True)

        return df

def consolidated_goalie_data():
    with conn.connect() as connection:
        pl_data = connection.execute("SELECT * FROM premier_league_goalie;").fetchall()
        pl_df = pd.DataFrame(pl_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','min','number_90s','GA','GA90','sota','saves','saveperc','w','d','l','cs','csperc','pkatt','pka','pksv','pkm','savepercpenalty'])


        la_liga_data = connection.execute("SELECT * FROM la_liga_goalie;").fetchall()
        la_liga_df = pd.DataFrame(la_liga_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','min','number_90s','GA','GA90','sota','saves','saveperc','w','d','l','cs','csperc','pkatt','pka','pksv','pkm','savepercpenalty'])

        bundesliga_data = connection.execute("SELECT * FROM bundesliga_goalie;").fetchall()
        bundesliga_df = pd.DataFrame(bundesliga_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','min','number_90s','GA','GA90','sota','saves','saveperc','w','d','l','cs','csperc','pkatt','pka','pksv','pkm','savepercpenalty'])


        ligue_1_data = connection.execute("SELECT * FROM ligue_1_goalie;").fetchall()
        ligue_1_df = pd.DataFrame(ligue_1_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','min','number_90s','GA','GA90','sota','saves','saveperc','w','d','l','cs','csperc','pkatt','pka','pksv','pkm','savepercpenalty'])


        serie_a_data = connection.execute("SELECT * FROM serie_a_goalie;").fetchall()
        serie_a_df = pd.DataFrame(serie_a_data,columns = ['index','Rk','Player','Nation','Pos','Squad','Age','Born','MP','Starts','min','number_90s','GA','GA90','sota','saves','saveperc','w','d','l','cs','csperc','pkatt','pka','pksv','pkm','savepercpenalty'])


        dfs = [pl_df,la_liga_df,bundesliga_df,ligue_1_df,serie_a_df]
        df = pd.concat(dfs)
        df.drop(['index','Rk'],axis=1,inplace=True)

        return df



def populate_mysql_table():
    table_name = 'Top_5_league_attack'
    attack_df = consolidated_attacker_data()
    attack_df.to_sql(con=conn, name=table_name, if_exists='replace')

    table_name = 'Top_5_league_defense'
    defense_df = consolidated_defender_data()
    defense_df.to_sql(con=conn, name=table_name, if_exists='replace')

    table_name = 'Top_5_league_goalie'
    goalie_df = consolidated_goalie_data()
    goalie_df.to_sql(con=conn, name=table_name, if_exists='replace')

    print("DATABASES POPULATED")

populate_mysql_table()


    

    




