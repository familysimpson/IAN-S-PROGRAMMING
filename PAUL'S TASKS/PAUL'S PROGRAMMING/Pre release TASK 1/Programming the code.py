"""Pre release task 1 practice 2
Generate a unique membership code for a new member of the club

PART 1
WRITE AN ALGORITHM USING STRUCTURED ENGLISH TO GENERATE A UNIQUE CODE FOR A NEW MEMBER

#INPUT the first name
#INPUT the middle name
#INPUT the last name

#INPUT the day of when member joins (Takes the day e.g 16/03/2018)
#WHILE the day entered is NOT the length of 2 digits
##OUTPUT "This must be ONLY two integer numbers"

#INPUT the number of the month (2 digits)
#WHILE length is NOT EQUAL to 1
##OUTPUT "This must be one integer"

#Create 2D array for the membership code
#OUTPUT "Here is your unique membership code", final

PART 2
CONVERT THIS STRUCTURED ENGLISH TO A FLOW CHART
(on paper)

PART 3
CONVERT THIS PSEUDOCODE
#DECLARE first_name: STRING
#DECLARE middle_name: STRING
#DECLARE last_name: STRING
#DECLARE member_start_day: INTEGER
#DELCARE member_start_month: INTEGER
#DECLARE final: ARRAY [1:1,1:5] OF OBJECT

INPUT first_name
INPUT middle_name
INPUT last_name

INPUT member_start_day
    WHILE LENGTH(member_start_day) <> 2:
    OUTPUT "This must be ONLY two integer numbers."
    END WHILE

INPUT member_start_month
    WHILE LENGTH(member_start_month) <> 1:
    OUTPUT "This must be ONLY one integer"
    END WHILE

final <- [[first_name[0], (middle_name[0]), (last_name[0]), (member_start_day), (member_start_month)]]

OUTPUT "Here is your unique membership code:", final

PART 4
THEN CONVERT THIS TO PROGRAM CODE IN PYTHON"""


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

final = [[first_name[0], (middle_name[0]), (last_name[0]), (member_start_day), (member_start_month)]]

print("Here is your unique membership code",final)