#Nicole Carrera #2DArray #Suduko

#DECLARE Suduko_array: ARRAY [0:2,0:2] OF INTEGER
#Suduko_array = [['' for r in range(0,3)]for c in range(0,3)]

#Suduko_array = [[0]*3] *3
#Suduko_array = [[0,0,0],
                # [0,0,0]]
#You could use either of these two in the comments^

Suduko_array = [[0 for r in range(3)] for c in range(3)]

import random

Suduko_array [0][0] = random.randint(1,9)
Suduko_array [0][1] = random.randint(1,9)
Suduko_array [0][2] = random.randint(1,9)
Suduko_array [1][0] = random.randint(1,9)
Suduko_array [1][1] = random.randint(1,9)
Suduko_array [1][2] = random.randint(1,9)
Suduko_array [2][0] = random.randint(1,9)
Suduko_array [2][1] = random.randint(1,9)
Suduko_array [2][2] = random.randint(1,9)

print(Suduko_array)