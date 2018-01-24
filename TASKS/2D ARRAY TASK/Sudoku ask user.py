#Nicole Carrera #2D array #24/01/18
#Ask the user for a number between 1 and 9 and display the array location (row and column)

number = input("Enter a number from 1 to 9")
while number != range(0,9):
    print("Incorrect. Enter again")

Sudoku_Array = [[number for r in range(3)] for c in range(3)]

print(Sudoku_Array)