#Nicole Carrera #AS computing class 1 01/11/17

#declare counter = INTEGER
#declare Teamname = STRING
#declare Playerhits = INTEGER
#declare Totalhits = INTEGER
#declare Averagehits = REAL
#declare PointsEarned = INTEGER

Counter = 0
Teamname ="Zeus"
Playerhits = 0
Totalhits = 0
Averagehits = 0.0
Pointsearned = 0

def get_details ():
    global Teamname, Playerhits,Totalhits
    Teamname= input("Enter team name")
    for counter in range(6,0,-1):
        Playerhits = int(input("Enter number of hits"))
        Totalhits = Totalhits + Playerhits


get_details()

def calc_hits ():
    global Averagehits, Pointsearned
    Averagehits = Totalhits/6
    if Totalhits > 50:
        Pointsearned = 1
    if Averagehits >= 10:
        Pointsearned = Pointsearned + 1

calc_hits()

print(Teamname, "has scored", Pointsearned)



