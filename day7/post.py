
# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com

"""import json
import requests

Host = "http://httpbin.org/post"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("http://httpbin.org/get?firstname=Dev&language=English")
    return response

print (get_method().text)
"""
import json
import requests
host="http://httpbin.org/post"
file=open("student.json","r")
file1=json.load(file)
data = file1

response = requests.post(host,data)
print(response.text)