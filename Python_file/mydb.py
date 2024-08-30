import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="besant"

)
#****my sql connection line *****
mycursor=mydb.cursor()
#********************************
def insert():
    sql="insert into student(regno,name,addr) values (%s,%s,%s)"
    regno=int(input("Enter regno"))
    name=input("Enter name")
    addr=input("Enter addr")
    val=(regno,name,addr)

#***************************
    mycursor.execute(sql,val)
#****************************
    mydb.commit() 

def view():
    mycursor.execute("select *from student where name='hari' ")
    myresult=mycursor.fetchall() 

    for i in myresult:
        print(i)
view()
 