#Database - Secret question(creation,insertion)

import mysql.connector
from mysql.connector import Error

def creation(cursor):
    mysql_database = ("CREATE DATABASE Secret;")

    mysql_table = """CREATE TABLE Secret_questions ( 
                                         Username varchar(255) PRIMARY KEY,
                                         Password varchar(255),
                                         Secrete_question varchar(255),
                                         Answer varchar(255)) """
    cursor = connection.cursor()
    cursor.execute(mysql_database)
    print("Database Created")
    cursor.execute("USE Secret")
    cursor.execute(mysql_table)
    print("Table Created")

def insertion(Username,Password,Secrete_question,Answer):
    mysql_insert = """INSERT into Secret_questions (Username,Password,Secrete_question,Answer) VALUES (%s,%s,%s,%s)"""
    values = (Username, Password, Secrete_question, Answer)
    cursor.execute(mysql_insert, values)
    cursor.execute("commit;")
    cursor.execute("select * from Secret_questions")
    result = cursor.fetchall()
    for i in result:
        print(i)
try:
    connection = mysql.connector.connect(host='localhost', username='root', password='Saisravan@25')
    cursor = connection.cursor()
except Error as e:
    print(e)

creation(cursor)
while True:
    Username = input("Enter Username : ")
    Password = input("Enter Password : ")
    Secrete_question = input("Enter Secrete_question to be kept : ")
    Answer = input("Enter Secret answer : ")
    insertion(Username,Password,Secrete_question,Answer)
    check = input("Do you want to insert more?Yes/No")
    if check=='N':
        break
