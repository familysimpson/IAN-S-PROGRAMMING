
#DECLARE femaleSalary: ARRAY [0:4] OF INTEGER
#DECLARE maleSalary: ARRAY [0:4] OF INTEGER
#DECLARE Salary: REAL
#DECLARE Gender: CHAR

femaleSalary = [0,0,0,0,0]
maleSalary = [0,0,0,0,0]

#line = "nicole,F,90000.00"
fh = open('Salary.TXT.py','r')
line = fh.readline()
while len(line) > 0:
    endpos = line.find(',')
    line= line[endpos+1:]
    endpos = line.find(',')
    gender = line[0:endpos]
    salary = float(line[endpos+1:])
    print(gender,salary)
    line = fh.readline()

    if salary >= 0 and salary <= 25000.0:
        elementID = 0

    elif salary > 25000.0 and salary <= 50000.0:
        elementID = 1

    elif salary > 50000.0 and salary <= 75000.0:
        elementID = 2

    elif salary > 75000.0 and salary <= 100000.0:
        elementID = 3

    elif salary > 100000.0 and salary <= 110000.0:
        elementID = 4

    if gender == "F":
            femaleSalary[elementID] = femaleSalary[elementID] + 1
    elif gender == "M":
            maleSalary[elementID] = maleSalary[elementID] + 1

print("Here is the number for the female salary", femaleSalary)
print("Here is the number for the male salary", maleSalary)