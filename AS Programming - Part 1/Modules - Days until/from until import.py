from until import*
#declare currDay : INTEGER
#declare currMonth : INTEGER
#declare futDay : INTEGER
#declare futMonth : INTEGER
#declare totalDays : INTEGER
#declare thisMonth : INTEGER
currDay = int(input("Enter curent day number"))
currMonth = int(input("Enter current month number"))
futDay = int(input("Enter future day number"))
futMonth = int(input("Enter future month number"))
totalDays = 0
for thisMonth in range(currMonth,futMonth+1):
    if thisMonth < futMonth:
        totalDays = totalDays + daysIn(thisMonth)
    else:
        totalDays = totalDays + daysUntil(currDay,futDay)
print(totalDays)