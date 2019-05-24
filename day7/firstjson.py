"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json

teacher_info=[{"First name":"R.S.",
               "Last Name":"Aggarwal",
               "Photo":"null",
               "Department":"Maths",
               "Research Areas":"Vedic maths",
               "Contact details": ["emailID","Phoneno"]
               },
               {"First name":"Jitu",
               "Last Name":"Bhaiyaa",
               "Photo":"https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwjh1L-B7JriAhXGXCsKHV8bDKcQjRx6BAgBEAU&url=https%3A%2F%2Ftwitter.com%2Ffarjigulzar&psig=AOvVaw08AtmgGXw6TijH_CsBoh91&ust=1557917208426318",
               "Department":"Maths",
               "Research Areas":"Vedic maths",
               "Contact details": ["emailID","Phoneno"]
               }
    ]

student_info=[{"First name":"Tom.",
               "Last Name":"cruise",
               "Photo":"null",
               "Department":"arts",
               "Research Areas":"filmograohy",
               "Contact details": ["emailID","Phoneno"]
               },
               {"First name":"Brad",
               "Last Name":"Pits",
               "Photo":"https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwjh1L-B7JriAhXGXCsKHV8bDKcQjRx6BAgBEAU&url=https%3A%2F%2Ftwitter.com%2Ffarjigulzar&psig=AOvVaw08AtmgGXw6TijH_CsBoh91&ust=1557917208426318",
               "Department":"Maths",
               "Research Areas":"Vedic maths",
               "Contact details": ["emailID","Phoneno"]
               }
    ]

file1=json.dumps(teacher_info)
file2=json.dumps(student_info)
with open("student.json","wt") as fp:
    json.dump(file2,fp)
with open("teacher.json","wt") as fp1:
    json.dump(file1,fp1)    