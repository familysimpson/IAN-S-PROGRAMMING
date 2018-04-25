i = 0
p = 0
k = 0
l = 0
g = 0

Salary = [0,0,0,0,0]

if Salary_Wage > 0 and Salary_Wage <= 25:
    Salary[1] = i + 1
elif Salary_Wage > 26 and Salary_Wage <= 50:
    Salary[2] = p + 1
elif Salary_Wage > 51 and Salary_Wage <= 75:
    Salary[3] = k + 1
elif Salary_Wage > 76 and Salary_Wage <= 100:
    Salary[4] = l + 1
elif Salary_Wage > 100 and Salary_Wage <= 110:
    Salary[5] = g + 1


fh = open("Salary.TXT.py","r")
line = fh.readline()
while len(line) > 0:
    print(line)
fh.close

