"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""
list1=[12,24,35,24,88,120,155,88,120,155]
"""lst1=set(list1)
l=list(lst1)
l=l[::-1]
print(l)"""

ll=[]
for item in list1:
    if item not in ll:
        ll.append(item)
print(ll[::-1])        