#higher/lower
#declare number1 : INTEGER
#declare number2 : INTEGER
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
if number1 > number2:
    print(number1,"is higher than",number2)
else:
    if number2 > number1:
        print(number1,"is lower than",number2)
    else:
        print("Both numbers are equal")