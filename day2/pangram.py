#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:16:44 2019

@author: root
"""

#pangram


str=input("enter your string")
str1=str.lower()
final_lst=[]
lst=[]
count=0
for i in str1:
    lst.append(i)
for j in lst:
    if j not in final_lst:
        final_lst.append(j)
for letter in final_lst:
    if letter in 'abcdefghijklmnopqrstuvwxyz':
        count+=1
if count==26:
    print("PANGRAM")
else:
    print("not PANGRAM")
                    
        


