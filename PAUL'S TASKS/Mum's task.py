"""
Write a program that allows user to select dish from a menu with price
The user can only select 3 dishes
Display the total price adn what they have ordered
 """

#DECLCARE Food_Array: ARRAY[0:4] OF STRING
#DECLARE Price_Array: ARRAY[0:4] OF REAL

Food_Array = ["","","","",""]

Food_Array[0] = "Chicken and Rice"
Food_Array[1] = "Turkey leg"
Food_Array[2] = "Ackee"
Food_Array[3] = "Salfish"
Food_Array[4] = "Cow foot"

Price_Array = [float,float,float,float,float]

Price_Array[0] = 2.50
Price_Array[1] = 4.00
Price_Array[2] = 6.50
Price_Array[3] = 3.50
Price_Array[4] = 1.50

print("Below is our menu:")

print(1,Food_Array[0],"...",Price_Array[0])
print(2,Food_Array[1],"...",Price_Array[1])
print(3,Food_Array[2],"...",Price_Array[2])
print(4,Food_Array[3],"...",Price_Array[3])
print(5,Food_Array[4],"...",Price_Array[4])

print("You can only select 3 dishes")

choice_1 = int(input("What  starter dish would you like? Please enter a number between 1 and 4:"))
if choice_1 == 1:
    print("1)", Food_Array[0], "...", Price_Array[0])
elif choice_1 == 2:
    print("2)", Food_Array[1], "...", Price_Array[1])
elif choice_1 == 3:
    print("3)", Food_Array[2], "...", Price_Array[2])
elif choice_1 == 4:
    print("4)", Food_Array[3], "...", Price_Array[3])
elif choice_1 == 5:
    print("5)", Food_Array[4], "...", Price_Array[4])

choice_2 = int(input("What main course dish would you like? Please enter a number between 1 and 4:"))
if choice_2 == 1:
    print("1)", Food_Array[0], "...", Price_Array[0])
elif choice_2 == 2:
    print("2)", Food_Array[1], "...", Price_Array[1])
elif choice_2 == 3:
    print("3)", Food_Array[2], "...", Price_Array[2])
elif choice_2 == 4:
    print("4)", Food_Array[3], "...", Price_Array[3])
elif choice_2 == 5:
    print("5)", Food_Array[4], "...", Price_Array[4])

choice_3 = int(input("What finishing dish would you like? Please enter a number between 1 and 4:"))
if choice_3 == 1:
    print("1)", Food_Array[0], "...", Price_Array[0])
elif choice_3 == 2:
    print("2)", Food_Array[1], "...", Price_Array[1])
elif choice_3 == 3:
    print("3)", Food_Array[2], "...", Price_Array[2])
elif choice_3 == 4:
    print("4)", Food_Array[3], "...", Price_Array[3])
elif choice_3 == 5:
    print("5)", Food_Array[4], "...", Price_Array[4])

print("Here is your total:")




