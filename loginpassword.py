import mysql.connector
from mysql.connector import Error

def validate_password(Password):
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    if len(Password) < 6 or len(Password) > 16:
        return False
    for x in Password:
        if x.isupper():
            count += 1
        elif x.islower():
            count1 += 1
        elif x.isdigit():
            count2 += 1
        elif x in ('$', '@', '&'):
            count3 += 1
        else:
            return False

    if count >= 1 and count1 >= 1 and count2 >= 1 and count3 >= 1:
        return True
    else:
        return False
