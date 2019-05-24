#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:59:17 2019

@author: root
"""

list=[10,101,11011,122]

for num1 in list:
    num=str(num1)
    b=num[::-1]
    if b==num:
       flag=true
    else:
        flag=false
print(flag)