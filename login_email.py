import mysql.connector
from mysql.connector import Error

import re

def decorator(func):
    def inner(Email_ID):
        pattern = '\w.+@[a-z]+\.com$'
        x = re.search(pattern,Email_ID)
        if x:
            return True
        else:
            return False
    return inner

@decorator
def simple_func(Email_ID):
    return Email_ID
