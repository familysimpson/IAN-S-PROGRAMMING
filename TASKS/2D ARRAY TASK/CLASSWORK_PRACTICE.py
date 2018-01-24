# 2D array footballgoals
# Nicole Carrera
# 18th January 2018

# DECLARE goals : ARRAY[0:3, 0:1] OF CHAR
#footballgoals = [['0' for r in range(0,4)]for c in range(0,2)]

footballgoals = [['Messi','2'],['Ronaldo','0'],['Benzema','-1'],['Finn','1']]
print(footballgoals)

index = 3
while index != -1:
    print(footballgoals[index][0])
    index = int(footballgoals[index][1])

#harcode the goals NICOLE NICOLE CARRERA