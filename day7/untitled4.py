#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:00:19 2019

@author: root
"""

import json
import requests
host="https://enichl0owfrql.x.pipedream.net"
file=open("student.json","r")
file1=json.load(file)
data = file1

response = requests.post(host,data)
print(response.text)