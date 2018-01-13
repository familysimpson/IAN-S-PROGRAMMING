import random

#declare name: ARRAY [5] OF STRING
name = [0,0,0,0,0,0]
age = [0,0,0,0,0,0]

no_names = 0
fh = open("File.py")
line = fh.readline()
while line != "":
    name[no_names] = line
    no_names = no_names + 1
    line = fh.readline()

fh.close()

#FILE HAS BEEN READ IN, NOW MANIPULATE VARIABLES

for index in range(0,6):
    num = random.randint(11,26)
    age[index] = num

#WRITE NEW FILE WITH NAME AND AGES

fh = open("Filenew.py","w")
for index in range(0,no_names):
    fh.write(name[index] + "," + str(age[index]) + chr(13))
fh.close()