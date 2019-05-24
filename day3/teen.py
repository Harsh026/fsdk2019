"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
sum=0
dict1={'a':0,'b':0,'c':0}
print("input three values")
dict1['a']=int(input("a"))
dict1['b']=int(input("b"))
dict1['c']=int(input("c"))
print(dict1)
for val in dict1.values():
    if val ==(15 or 16):
        sum=sum+val
        
    elif val in range(13,20):
        continue
    else:
        sum=sum+val
print("Your sum is", sum)        
        
