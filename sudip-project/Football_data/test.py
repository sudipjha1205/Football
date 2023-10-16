import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://fbref.com/en/comps/20/passing/Bundesliga-Stats"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

table1 = soup.find('table', id='stats_keeper')
#print(table1)

headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

print(headers)
'''
teams = headers[(len(headers) - 20):]
print(teams)
headers = ['# Pl', 'MP', 'Starts', 'Min', '90s', 'GA', 'GA90', 'SoTA', 'Saves', 'Save%', 'W', 'D', 'L', 'CS', 'CS%', 'PKatt', 'PKA', 'PKsv', 'PKm', 'Save%']

mydata = pd.DataFrame(columns = headers)
rows = []

for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    #print(row_data)
    row = [i.text for i in row_data]
    rows.append(row)
    #print(row)
    #length = len(mydata)
    #mydata.loc[length] = row

rows.pop(0)
print("lenght",len(rows))
mydata = pd.DataFrame(rows,columns = headers)
mydata.insert(0,"Squad",teams)
print(mydata)
'''
