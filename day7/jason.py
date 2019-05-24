"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import requests

city = input("enter city name")
str1="?q="
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = str1+city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"



url=url1+url2+url3
response=requests.get(url)
print(response.text())