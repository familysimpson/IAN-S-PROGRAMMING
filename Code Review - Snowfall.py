#DECLARE line : STRING
#DECLARE snowfall: ARRAY[1:12] OF INTEGER
#DECLARE month: INTEGER
#DECLARE highestMonth: INTEGER

month = 1
snowfall =[]
heaviest = -1

FileHandle = open("snowfall.txt.py","r")
Line = FileHandle.readline()
while len(Line) > 0:
    snowfall[month]= Line
    month = month + 1
    if snowfall[month] > heaviest:
        heaviest = Line
    Line = FileHandle.readline()
FileHandle.close
print("The heaviest snowfall was "+ str(heaviest) +" inches.This happened in month number")