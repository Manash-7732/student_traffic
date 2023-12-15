from flask import Flask, render_template
import mysql.connector
#import time
app = Flask(__name__)

@app.route('/')
def index():
    var=mysql.connector.Connect(
    host='172.17.0.1',
    user='root',
    password='root',
    database='manash',
    port=3311
    )

    curso=var.cursor()
    select_query = "SELECT * FROM students"
    curso.execute(select_query)
    
    students = curso.fetchall()

    #print(students)
    return render_template('boot.html', students=students)  
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0') 