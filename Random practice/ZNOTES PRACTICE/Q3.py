"""Write a program that evaluates an input and sees whether it is equal to , less than , or greater than a constant
value of your choice """

import random
mysterynumber = random.randint(0,100)

print("This program will see if your number is less than or greater than the random generated number. This number will be between 0 and 100")

new = int(input("Enter a number:"))
while new > 100 or new < 0 :
    print("You must input values between 0 and 100")
    new = int(input("Enter a number:"))

if new == mysterynumber:
    print("Your number is equal to the mystery number")
elif new < mysterynumber:
    print("Your number is less than the mystery number")
elif new > mysterynumber:
    print("Your number is greater than the mystery number")

print("The mystery number is:", mysterynumber)

