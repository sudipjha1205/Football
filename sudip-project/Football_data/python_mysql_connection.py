import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sudip",
  password="Sud1p@jh@",
  database='football'
)

cursor = mydb.cursor()

table_name = "premier_league_attackers"
cursor.execute("select * from {} limit 10;".format(table_name))

print(cursor.fetchall())
#tables = [column[0] for column in cursor.fetchall()]

for table in tables:
    cursor.execute("SHOW columns FROM {}".format(table))
    print(table)
    print([column[0] for column in cursor.fetchall()])
