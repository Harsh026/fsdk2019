from bs4 import BeautifulSoup
import requests
#import urllib



#specify the url
url1 = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url1).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

_table=soup.find('table', class_='table')



#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
tb=_table.find("tbody")

for row in tb.findAll('tr'):
    cells = row.findAll('td')
        
    A.append(cells[0].text.strip())
    B.append(cells[1].text.strip())
    C.append(cells[2].text.strip())
    D.append(cells[3].text.strip())
    E.append(cells[4].text.strip())
        
import pandas as pd
from collections import OrderedDict

col_name = ["position","team","weighted matches","points","rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("team.csv")