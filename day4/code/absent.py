"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

counter=0
with open("absentee.txt","wt") as fp:
    while counter<25:
        
        print("enter name of student :")
        name=input()
        if not name:
            break
        else:
            fp.write(name+"\n")
        counter=counter+1