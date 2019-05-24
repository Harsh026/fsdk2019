"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""





l1=[1,3,6,78,35,55]
l11=set(l1)
l2=[12,24,35,24,88,120,155]
l22=set(l2)
l3=l11.intersection(l22)
print(l3)
