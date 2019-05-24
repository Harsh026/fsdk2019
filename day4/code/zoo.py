"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
import csv

def csv_reader():
    with open("zoo.csv","r") as file1:
        csv1=csv.reader(file1,delimite=",")
        for line in csv1:
            print(line)
def name():
    with open("zoo.csv",) as file1: 
        csv1=csv.reader(file1,delimiter=",") 
        lst=[]
        for i in csv1:
            if i[0] not in lst:
                lst.append(i[0])
        print(lst)        

def water():
    with open ("zoo.csv") as zoo:
        dict1={}
        csv_reader=csv.reader(zoo, delimiter=",")
        for item in csv_reader:
            if item[0]=="tiger":
                key="tiger"
                if key in dict1:
                    dict1[key]=int(dict1[key])+int(item[2])
                else:
                    dict1[key]=int(item[2])
            if item[0]=="elephant":
                    key1="elephant"
                    if key1 in dict1:
                        dict1[key1]=int(dict1[key1])+int(item[2])
                    else:
                        dict1[key1]=int(item[2])
            if item[0]=="kangaroo":
                    key1="kangaroo"
                    if key1 in dict1:
                        dict1[key1]=int(dict1[key1])+int(item[2])
                    else:
                        dict1[key1]=int(item[2])  
            if item[0]=="zebra":
                    key1="zebra"
                    if key1 in dict1:
                        dict1[key1]=int(dict1[key1])+int(item[2])
                    else:
                        dict1[key1]=int(item[2]) 
            if item[0]=="lion":
                    key1="lion"
                    if key1 in dict1:
                        dict1[key1]=int(dict1[key1])+int(item[2])
                    else:
                        dict1[key1]=int(item[2])               
        print(dict1)  

4
                       
def  water_needed(file):
    with open("zoo.csv") as file1: 
        csv1=csv.reader(file1,delimiter=",") 
        next(csv1)
        sum=0
        
        for i in csv1:
            temp=0
            temp=i[2]
            sum=sum+int(temp)
        print("total water needed is :",sum)    
    