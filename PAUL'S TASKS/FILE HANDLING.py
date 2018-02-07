"""
TASK1
Create text file called temp.txt.py
Input a string from the keyboard and write it into the file
Close the file


EXTENSION
Allow multiple strings to be input
Allow multiple string to be read from file

"""
LineOfText = input("Hello world, Enter your name")
FileHandle = open("temp.txt.py","w")
FileHandle.write(LineOfText)
FileHandle.close


