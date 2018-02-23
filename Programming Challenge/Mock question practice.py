#DECLARE day: INTEGER
#DECLARE noExams: INTEGER
noExams = 0

input("Do you have an exam?")
for counter in range(0,7):
    if noExams == "yes" or "Yes" or "y":
        noExams2 = noExams + 1
    else:
        noExams2 = noExams + 0
    print("You have",noExams2,"goodluck!!")




