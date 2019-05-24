#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:36:48 2019

@author: root
"""
"""def pallendrome1(x):
    
    if x==x[::-1]:
        print ("True")
    else:
        print("false")
lsit1=input("Enter comma seperated integer")
lst=lsit1.split(",")
s=list(map(pallendrome1,lst))
print(s)"""




lsit1=input("Enter comma seperated integer")
lst=lsit1.split(",")
s=any(list(map(lambda x:True if x==x[::-1] else False,lst)))
print(s)