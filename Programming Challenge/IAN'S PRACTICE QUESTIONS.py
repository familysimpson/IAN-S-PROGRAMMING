
day = 0
noExams = 0

for counter in range (0,7):
    examday = input("Do you have an exam on this day?")
    if examday == "Yes" or "yes" or "Y":
         noExams = noExams + 1
    else:
        noExams = noExams + 0
print("You have",noExams, "exams. Goodluck!")




