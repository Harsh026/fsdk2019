
"""
Challenge 3
Read the words from a file

"""

filename=input("Enter the name of the file")
file_object= open(“filename.__path__”, “r”)
for line in file_object:
    print(line)