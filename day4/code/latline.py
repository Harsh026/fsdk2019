"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
file_name=input("enter the name of text file")
with open(file_name,"r") as fp:
    
    a=fp.readlines()
    b=a[-1]
    print(b)