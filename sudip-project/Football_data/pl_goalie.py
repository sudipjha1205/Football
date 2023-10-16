import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd


url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

comments = soup.find_all(string=lambda text: isinstance(text, Comment))

tables = []
for each in comments:
    if 'table' in each:
        try:
            tables.append(pd.read_html(each)[0])
        except:
            continue

print(tables)
