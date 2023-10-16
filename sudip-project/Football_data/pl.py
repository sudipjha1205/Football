import requests
from lxml import etree
from bs4 import BeautifulSoup

res = requests.get("https://fbref.com/en/comps/9/stats/Premier-League-Stats")
soup = BeautifulSoup(res.content,'html.parser')
soup_dom = etree.HTML(str(soup))

#tree = etree.fromstring(res.content)
#tree.xpath('.//div[@class="teamInfo"]/text()')

for div in soup.findAll('table', attrs={'class':'min_width sortable stats_table shade_zero now_sortable sticky_table eq2 re2 le2 is_sorted'}):
    print(div.text)
