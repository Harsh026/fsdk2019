
"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

week=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days=input("enter comma seperated tuple of names of week days")
days1=days.split(",")
print(days1) 
tup1=set(week).difference(set(days1))
tup2=tup1.union(days1)
print(tuple(set(tup2)))   
    