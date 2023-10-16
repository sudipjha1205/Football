import mysql.connector
from sqlalchemy import create_engine
from contextlib import closing

username='sudip'
password='Sud1p@jh@'
host='localhost:3306'
database_name='football'

connection = "mysql+mysqlconnector://{}:{}@{}/{}".format(username,password,host,database_name)
cnx = create_engine(connection)
con = cnx.raw_connection()

try:
    with closing(con.cursor()) as cursor:
        cursor.callproc('more',['neymar'])

        data = []
        for sr in cursor.stored_results():
            columns = [column[0] for column in sr.description]
            ds = sr.fetchall()

            dataset = []
            dataset.append(columns)
            for row in ds:
                dataset.append(list(row))

            data.append(dataset)
            sr.close()
        cursor.close()

        import pprint
        pprint.pprint(data)

except Exception as e:
    print( f'Exception. Type {type(e)}: {str(e)}' )
finally:
    if 'connection' in locals():
        con.close()
'''
cursor.execute('call more("neymar");')
lst = cursor.fetchall()
cursor.close()
for i in lst:
    print(lst)
    '''

