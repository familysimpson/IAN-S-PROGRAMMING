#Populate all elements of a 5x5 2D array with the letter “M”
#Randomly generate the row and column position and change this array element to the letter “W”
#Display the grid on the screen
#Repeatedly ask the user for a valid row and column and let them know if they have found Wally.
#End the program when the user finds Wally.

#DECLARE index: INTEGER

Where_Wally = [["M" for r in range (5)]for c in range (5)]

import random

Where_Wally[random.randint(0,4)][random.randint(0,4)] = 'W'

endGame = False
while endGame != True:
    rowGuess = int(input("Enter a number from 1 to 5"))
    while rowGuess < 0 or rowGuess > 5:
        print("Incorrect. Enter again")
        rowGuess = int(input("Enter a number from 1 to 5"))

    colGuess = int(input("Enter a number from 1 to 5"))
    while colGuess < 0 or colGuess > 5:
        print("Incorrect. Enter again")
        colGuess = int(input("Enter a number from 1 to 5"))

    if Where_Wally[rowGuess][colGuess] == 'W':
                print("You won")
                endGame = True
    else:
        print("Incorrect")

