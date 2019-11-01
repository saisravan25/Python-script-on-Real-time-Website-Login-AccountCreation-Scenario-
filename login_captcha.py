import random

def captcha():
    ops = ['+', '-', '//', '*']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    random_operation = random.choice(ops)

    print("Captcha : ", num1, random_operation, num2)
    maths = eval(str(num1) + random_operation + (str(num2)))
    Answer = int(input("Enter result of captcha"))
    if Answer == maths:
        return True
    else:
        return False
