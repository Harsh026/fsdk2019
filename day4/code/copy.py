"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

filename=input("Enter the name of the file you want to copy")
filename2=input('Enter name of the file in which you want to copy file')


try:
    file = open("filename",  "rt" )
    print (file.name)
except IOError:
    print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")
finally:
    file2=open('filename2',"wt")
    for line in file:
        file2.write(line)
    file2.close()    
    file.close() 



    
    
    