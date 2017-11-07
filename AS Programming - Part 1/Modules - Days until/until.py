def daysUntil(start, target):
    return target - start

def daysIn(month):
    #declare noDays : INTEGER
    if (month == 4) or (month == 6) or (month == 9) or (month == 11):
        noDays = 30
    else:
        if (month == 2):
            noDays = 28
        else:
            noDays = 31
    return noDays
