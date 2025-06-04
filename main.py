from db import connect
def main():
    con=connect()
    cursor=con.cursor()
    print("""\n main menu:
1. add student
2. add faculty
3. feedback
4. logout""")
    ch=int(input("enter your choice: "))
    if ch==1:
        add_student()
    elif ch==2:
        add_faculty()
    elif ch==3:
        feed_back()
    elif ch==4:
        print("logout")
    else:
        print("invalid choice")
def add_student():
    con=connect()
    cursor=con.cursor()
    std_id=input("enter student_id: ")
    name=input("enter the name: ")       
    branch=input("enter branch name: ")
    email=input("enter the email: ")
    query="insert into student(std_id,name,branch,email) values(%s,%s,%s,%s)"
    values=(std_id,name,branch,email)
    cursor.execute(query,values)
    con.commit()
    print("student added succesfully.")

def add_faculty():
    con=connect()
    cursor=con.cursor()
    faculty_id=input("enter faculty_id: ")
    name=input("ente name: ")
    query="insert into faculty(faculty_id,name) values(%s,%s)"
    values=(faculty_id,name)
    cursor.execute(query,values)
    con.commit()
    print("faculty added succesfully.")

def feed_back():
    con=connect()
    cursor=con.cursor()
    feed_back_id=input("enter feedback_id: ")
    std_id=input("enter std_id: ")
    faculty_id=input("enter faculty_id: ")
    rating=int(input("enter your rating from 1 to 5: "))
    if rating < 1 or rating > 5:
        return
    comments=input("enter text: ")
    query="insert into feedback(feedback_id,faculty_id,rating,comments) values(%s,%s,%s,%s)"
    values=(feed_back_id,faculty_id,rating,comments)
    cursor.execute(query,values)
    con.commit()
    print("feedback submitted succesfully.")

main()
