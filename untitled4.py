# -*- coding: utf-8 -*-
"""
Anna Ganguly
Gencyber 2016
Loops.py
7/7/16
"""

"""import random

myint = 465

while myint > 400:
    
    print(myint)"""
    
'''guess = int(input("Guess my number"))
number = random.randint(0,100)

while guess != number:
    if number < guess:
        print("This number is too big")
    else:
        print("This number is too small")
    guess = int(input("Guess again"))

print("You are correct!")'''

"""guess = input("Guess my password")
password = "PIES"

while guess != password :
    print("Sorry, but that is incorrect")

    guess = input("Guess again")

print("You are correct!")"""

'''for i in range(1,11):
    print(i)

string = "Do you wanna build a snowman"

for char in string:
    print(char)'''

"""def ascii_eight_bit(letter):
    num = ord(letter)
    bitstring=""
    for i in range(8):
        print(num)
        if num % 2 == 0:
            bitstring = '0' +bitstring
            print('0')
        else:
            bitstring = '1' +bitstring
            print('1')
        num = num //2
    return bitstring
    
print(ascii_to_eight_bit('S'))"""



'''def password_check(password):
    if len(password) >= 6:
        for char in "password":
            if ord(char) > 65 and ord(char)< 90:
                hasUpper = True
    elif ord(char) >= 97 and ord(char) <= 65  
            hasLower = True
            if hasUpper == True and hasLower == True:
                return True
            else:
                return False
    else:
        return False
    

password_check("Lmnopq")'''
    

    