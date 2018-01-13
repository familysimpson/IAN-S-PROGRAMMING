#DECLARE name: ARRAY [5] OF STRING

name = [0,0,0,0,0]

name[0] = "Jesus"
name[1] = "Gus"
name[2] = "Debbie"

no_names = 3

fh = open("output.py","w")
for index in range(0, no_names):
    fh.write(str(name[index]) + chr(13))
fh.close()
