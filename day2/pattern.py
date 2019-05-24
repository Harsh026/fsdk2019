#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:22:05 2019

@author: root
"""

# Pattern Builder
num= input("enter a number")
num=int(num)
for i in range(1,num+1):
    print("*"*i)
    
for j in range(1,num+1):
    print("*"*(num-j))
        
        