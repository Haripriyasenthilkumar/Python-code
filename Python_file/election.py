import mysql.connector
import smtplib

# Establish the MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="election"
)

cursor = db.cursor()

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    candidate VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    name VARCHAR(255) PRIMARY KEY,
    vote_count INT
)
""")

def display():
    candidate=["candidate_A","candidate_B","candidate_c"]
    print("\n list of candidate")
    for i in candidate:
        print(i)
    



def email_msg(email):
    try:
        s=smtplib.SMTP('smtp.gmsil.com',587)
        s.startls()
        s.login("225027054@sastra.ac.in","xfiz lcib hdib sqnf")
        msg=(f" thankyou for vote")
        s.sendmail("225027054@sastra.ac.in",email,msg)
        s.quit()
        print("Email sent successfully!")
        
    except :
        print("Fail to send")

def add_vote(candidate_name):
    cursor.execute("SELECT vote_count FROM candidates WHERE name=%s", (candidate_name,))
    result = cursor.fetchone()
    if result:
        current_count = result[0]
        cursor.execute("UPDATE candidates SET vote_count = %s WHERE name = %s", (current_count + 1, candidate_name))
    else:
        cursor.execute("INSERT INTO candidates (name, vote_count) VALUES (%s, %s)", (candidate_name, 1))
    db.commit()

def add_user(name, email, candidate):
    cursor.execute("INSERT INTO users (name, email, candidate) VALUES (%s, %s, %s)", (name, email, candidate))
    db.commit()

def main():
    
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    display()
    candidate = input("Enter your favorite candidate: ")
    add_user(name, email, candidate)
    add_vote(candidate)
    email_msg(email)


       


main()

# Close the connection
db.close()