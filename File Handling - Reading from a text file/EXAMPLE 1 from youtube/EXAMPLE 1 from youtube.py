#DECLARE line AS STRING
FileHandle = open("example.txt.py", "r")
for counter in range(1,11):
    line = FileHandle.readline()
    print(line)
FileHandle.close