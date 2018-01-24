#Populate all elements of a 5x5 2D array with the letter “M”
#Randomly generate the row and column position and change this array element to the letter “W”
#Display the grid on the screen
#Repeatedly ask the user for a valid row and column and let them know if they have found Wally.
#End the program when the user finds Wally.

#DECLARE index: INTEGER

Where_Wally = [["M" for r in range (5)]for c in range (5)]
for index in range (0,5):
    print(Where_Wally)

