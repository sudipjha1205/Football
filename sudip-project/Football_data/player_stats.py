import requests
import pandas as ps
from bs4 import BeautifulSoup

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"

r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')

table1 = soup.find('table',id="stats_standard")
print(table1)
