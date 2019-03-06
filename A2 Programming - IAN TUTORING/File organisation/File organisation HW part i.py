

"""Create a Python program that generates 1000 randomly generated integers between 1 and 99.
Create two files: an ASCII file and a binary file. Both should stores each number separated by a comma."""

#DECLARE j,i: INTEGER
#DECLARE NumbersArray: ARRAY[0:1000] OF INTEGER
#DECLARE message: STRING (That holds the integer value but have to make it a string for ASCII file)

import random
j = random.randint (1,99)
NumbersArray = [""] * 1000
ASCII_file = open("Numbers1to99.txt", "w")
binary_file = open("Numbers1to99TEST2", "wb") # wb not w
for i in range(0,1000):
    NumbersArray[i] = j
    j = random.randint(1, 99)
    message = str(NumbersArray[i]) + ","+"\n"
    binary_message = (message).encode('utf8')  # these lines just prove the data is in bytes
    ASCII_file.write(message)
    binary_file.write(binary_message)  # write bytes to file
ASCII_file.close()
binary_file.close()
