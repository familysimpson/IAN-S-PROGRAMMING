"""
TASK2
Open the file "temp.txt.py"
Read the string from the file
Display the string on the screen
"""

FileHandle = open("temp.txt.py","r")
LineOfText = FileHandle.readline()
print(LineOfText)
FileHandle.close