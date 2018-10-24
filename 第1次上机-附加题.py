import re
import random

digits = [chr(i) for i in range(48, 58)]
digits = "".join(digits)
upper_letter = [chr(i) for i in range(65, 91)]
upper_letter = "".join(upper_letter)
lower_letter = [chr(i) for i in range(97, 123)]
lower_letter = "".join(lower_letter)
operator=[chr(i) for i in range(33,48)]
operator="".join(operator)+str(chr(i) for i in range(58,65))
operator=operator+str(chr(i) for i in range(91,97))
operator=operator+str(chr(i) for i in range(123,127))

l = [chr(i) for i in range(33, 127)]
l = "".join(l)
lletterflag = False
uletterflag = False
numflag = False
operatorflag = False

passwordlib = []
n = input("请问您想要多少位的密码呢！（八位以上哦")
while 1:
    if n.isdigit() and int(n) > 8:
        password = random.sample(l, int(n))

    for i in password:
        if i in digits:
            numflag = True
            continue
        elif i in lower_letter:
            lletterflag = True
        elif i in upper_letter:
            uletterflag = True
        elif i in operator:
            operatorflag = True
    count = 0
    oldpassword = "by99YL17!"
    for i in password:
        if i in oldpassword:
            count = count + 1

    if numflag & lletterflag & uletterflag & operatorflag and count <= 3:
        passwordlib.append(password)
        oldpassword = "".join(password)
        print(oldpassword)
        break
