"""
EXTENSION 1
Allow multiple strings to be input
"""

LineOfText = input("")
FileHandle = open("temp.txt.py","w")
FileHandle.write(LineOfText)
FileHandle.close