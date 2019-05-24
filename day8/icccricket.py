"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""


from bs4 import BeautifulSoup
import  requests
import pandas as pd
from collections import OrderedDict



link="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
site=requests.get(link).text
soup= BeautifulSoup(site,"lxml") 
_table=soup.find('table', class_='table')

A=[]
B=[]
C=[]
D=[]
E=[]
tb=_table.find('tbody')

for row in tb.findAll('tr'):
    cells = row.findAll('td')
   
    
    A.append(cells[0].text.strip())
    B.append(cells[1].text.strip())
    C.append(cells[2].text.strip())
    D.append(cells[3].text.strip())
    E.append(cells[4].text.strip())
    
col_name = ["Position","Team Name","Weighted Matches","","Point","Rating"]
Scrapped_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(Scrapped_data) 
df.to_csv("Teams_data.csv")
   
    
    