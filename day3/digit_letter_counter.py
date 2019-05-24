
"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
dic={'digit':0,'letter':0}
letter='abcdefghijklmnopqrstuvwxyz'
digit='1234567890'
str=input("enter your string")
for item in str:
    if item in letter:
        dic['digit']=dic['digit']+1
    if item in digit:
        dic['letter']=dic['letter']+1
print(dic)       
        