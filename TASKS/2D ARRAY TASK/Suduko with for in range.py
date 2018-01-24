#Nicole Carrera #2DArray #Suduko #22/01/18
#Populate a 3x3 2D array with numbers between 1 and 9 (each number occurs only once)

#DECLARE Suduko_array: ARRAY [0:2,0:2] OF INTEGER
#Suduko_array = [['' for r in range(0,3)]for c in range(0,3)]

#1)Suduko_array = [[0]*3] *3
#2)Suduko_array = [[0,0,0],
                # [0,0,0]]
#You could use either of these two in the comments^

Suduko_array = [[0 for r in range(3)] for c in range(3)]

import random

def exist(num):
    myBool = False
    for row in range(0,3):
        for col in range(0,3):
            if Suduko_array[row][col] == num:
                myBool = True
    return myBool

for row in range (0,3):
    for column in range (0,3):
        added = False
        while added != True:
            temp = random.randint(1,9)
            if exist(temp) != True:
                print('adding ',temp)
                Suduko_array[row][column] = temp
                added = True
            else:
                print(temp,'there already')

#DECLARE index: INTEGER
#this is to display it as a table

for index in range (0,3):
    print(Suduko_array[index])
