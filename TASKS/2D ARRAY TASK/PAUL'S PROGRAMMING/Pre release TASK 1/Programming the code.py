#Take first name take the first letter of the first name
#Take middle name take the first letter of the middle name
#Take last name and take the first letter of the last name
#This will generate first 3 letters of alphanumeric code

#Take the date of when user joins member (on the system)
#Takes the day e.g 16/03/2018
#Takes the day
#Takes the last number of the month e.g 03 --> Takes 3


first_name = str(input("Input first name of new member:"))
middle_name = str(input("Input middle name of new member. If member does not have surname input 'N':"))
last_name = str(input("Input surname of new member:"))

member_start_day = str(input("Input start day as a number e.g. 16 or 12 or 02:"))
while len(str(member_start_day)) != 2:
    print("This must be ONLY two integer numbers.")
    member_start_day = int(input("Input start day e.g. 16 or 12 or 02:"))

member_start_month = str(input("Input start month as a number:"))
while len(str(member_start_month)) != 1:
    print("This must be ONLY one integer.")
    member_start_month = str(input("Input start month as a number:"))

final = print(first_name[0]), print(middle_name[0]), print(last_name[0]), print(member_start_day), print(member_start_month)

Board = [[final for i in range (5)] for j in range(1)]
print(Board)