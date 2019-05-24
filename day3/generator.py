#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:49:50 2019

@author: root
"""
def func(lst):
   
     lst1=lst.split(",")
     return (list(lst1),tuple(lst1))
    

lst=input("Input  comma seperated numbers")
print(func(lst))