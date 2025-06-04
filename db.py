import mysql.connector
def connect():
    conn= mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_feedback"
    )
    return conn
if(connect()):
    print("connection established succesfully")
else:
    print("connection failed")



    