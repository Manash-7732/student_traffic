import mysql.connector
from faker import Faker
#from flask import Flask, render_template
import time
#app = Flask(__name__)

#from myconnection import conn

# cur=conn()
# cur_my=cur.cursor()
# print("cur",cur_my)
# cur_my.execute("Show databases")
var=mysql.connector.Connect(
    host='172.17.0.1',
    user='root',
    password='root',
    database='manash',
    port=3311
)
print(var)
fake=Faker()

curso=var.cursor()

create_table_query ="""
    CREATE TABLE IF NOT EXISTS students 
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        enrollment_date DATE
    )
"""
#curso=conn()
print("conn",curso)
#var=conn()
curso.execute(create_table_query)
var.commit()

while True:
     student_name = fake.name()
     student_email = fake.email()
     enrollment_date = fake.date()
     insert_query = "INSERT INTO students (name, email, enrollment_date) VALUES (%s, %s, %s)"
     time.sleep(2)
     data = (student_name, student_email, enrollment_date)
     curso.execute(insert_query, data)
     print (data)
     var.commit(),