
"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""


import requests

amount=input("Enter the amount")
amount=int(amount)

url1="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=3f76a8efcff1260f96f6"
response=requests.get(url1)
response=response.json()
amount=amount*response["USD_INR"]
print(amount)


