import mysql.connector
from mysql.connector import Error
import signup
import login_captcha

def Login(username,cursor,password):
        username = username
        mysql_select = """select * from Secret_questions where username=%s"""
        cursor.execute("USE Secret")
        cursor.execute(mysql_select,(username,))
        result = cursor.fetchall()
        if result:
            cursor.execute("select password from Secret_questions where username=%s",(username,))
            output = cursor.fetchone()
            if password in output:
                if login_captcha.captcha():
                    print("Login successful")
                else:
                    print("Incorrect captcha")
            else:
                print("username or password incorrect")
                secret_ques = input("Answer secret questions : yes/no")
                if secret_ques=='yes':
                    cursor.execute("select Secrete_question,Answer from Secret_questions where username=%s",(username,))
                    output = cursor.fetchone()
                    print("Secret question : ",output[0])
                    Answer = input("Enter Answer")
                    if Answer in output:
                        print("Successful\nEmail has been sent to your registered mail id for changing password")
                    else:
                        print("Incorrect details")
                else:
                    print("Signup for a new account")
        else:
            print("Please enter a valid username or create a new account")
            signup_new = input("Create a new account : yes/no")
            if signup_new=='yes':
                print("Sign up")
                signup.insertion_signup(cursor)
            else:
                print("Please signup for account creation")

connection = mysql.connector.connect(host='localhost', username='root', password='Saisravan@25')
cursor = connection.cursor()
username = input("Enter username")
password = input("Enter Password")
Login(username,cursor,password)
#After successful login or signup your connection(usage) will be closed in Database
if connection.is_connected():
    cursor.close()
    connection.close()
