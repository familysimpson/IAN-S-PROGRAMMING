# code to define a record
class record:
    def __init__(self, word, points):
        self.word = word
        self.points = points

ASCII_file = open("words.txt", "r")
line = ASCII_file.readline()
i = 0
rec = [] * i
while len(line) > 0:
    i = i + 1
    rec[i] = record(line, len(line))
    rec = [] * i
ASCII_file.close()