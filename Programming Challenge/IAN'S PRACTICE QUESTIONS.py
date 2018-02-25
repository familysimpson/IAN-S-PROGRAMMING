#DECLARE day: INTEGER
#DECLARE noExams: INTEGER
#DECLARE day_name: ARRAY (0:6) OF STRING

day = 0
noExams = 0
day_name = ["","","","","","",""]

day_name[0] = "Monday"
day_name[1] = "Tuesday"
day_name[2] = "Wednesday"
day_name[3] = "Thursday"
day_name[4] = "Friday"
day_name[5] = "Monday"
day_name[6] = "Tuesday"

for counter in range (0,7):
    print("Please answer with 'Yes/y/Y/yes' if you have an exam on",day_name[counter])
    examday = str(input())
    if examday == "Yes" or examday == "Y" or examday == "yes" or examday == "y":
        noExams = noExams + 1
print("You have",noExams, "exam/s. Goodluck!")



