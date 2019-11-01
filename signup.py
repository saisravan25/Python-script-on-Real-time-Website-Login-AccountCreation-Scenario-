import mysql.connector
from mysql.connector import Error
import loginpassword
import login_email

def insertion_signup(cursor):
    Username = input("Enter Username")
    Password = input("Enter Password")
    Secrete_question = input("Enter Secrete_question")
    Answer = input("Enter Answer")
    Email_ID = input("Enter Email_ID")
    if loginpassword.validate_password(Password):
        if login_email.simple_func(Email_ID):
            mysql_signup = """INSERT INTO Secret_questions (Username,Password,Secrete_question,Answer,Email_ID) VALUES (%s,%s,%s,%s,%s)"""
            signup_values = (Username, Password, Secrete_question, Answer, Email_ID)
            cursor.execute(mysql_signup, signup_values)
            cursor.execute("commit;")
            print("Account created successfully")
        else:
            print("Please enter a valid Email_ID")
    else:
        print("Password crieteria not matching")
