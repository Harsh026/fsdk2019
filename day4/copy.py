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
    file1=open(filename,"r" )
    print(file1.name)
except IOError:
    print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")
finally:
    file2=open(filename2,"w")
    for line in file1:
        file2.write(line)
    file2.close()    
    file1.close() 



    
    
    