import mysql.connector
from pandas import DataFrame


conn = mysql.connector.connect( user='root', password='', host='localhost')
c = conn.cursor()


c.execute("CREATE DATABASE students1;")
c.execute("USE students1;")


c.execute ("""CREATE TABLE students1(
          Student_name TEXT ,
          Student_age  INTEGER,
          Student_rollno INTEGER,
          Student_branch TEXT
          )""")


c.execute("INSERT INTO students1 VALUES ('Sylvester', 12, 56 ,'it')")
c.execute("INSERT INTO students1 VALUES ('Yogendra',13 , 70,'cse')")
c.execute("INSERT INTO students1  VALUES ('Pradeep',14 , 30,'ee')")
c.execute("INSERT INTO students1 VALUES ('Kunal',12 , 45,'ece')")
c.execute("INSERT INTO students1 VALUES ('Devendra',13 , 34,'cse')")
c.execute("INSERT INTO students1 VALUES ('utkarsh',13 , 66,'it')")
c.execute("INSERT INTO students1 VALUES ('ram',13, 76,'it')")
c.execute("INSERT INTO students1 VALUES ('virat',15 , 89,'it')")
c.execute("INSERT INTO students1 VALUES ('rohan',12 , 41,'it')")
c.execute("INSERT INTO students1 VALUES ('tarun',13 , 44,'ece')")





c.execute("SELECT * FROM students1")


df = DataFrame(c.fetchall())
df.columns = ["name","age","rollno","branch"]


conn.commit()

conn.close()
