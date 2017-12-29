#DECLARE line AS STRING
FileHandle = open("example2.txt.py", "r")
line = FileHandle.readline()
while len(line) > 0:
    print(line)
    line = FileHandle.readline()
FileHandle.close