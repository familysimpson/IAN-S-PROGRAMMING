
"""
DECLARE femaleSalary: ARRAY [0:4] OF INTEGER
DECLARE maleSalary: ARRAY [0:4] OF INTEGER
DECLARE Salary: REAL
DECLARE Gender: CHAR

FemaleSalary[0:4] = 0
MaleSalary[0:4] = 0

OPENFILE "Salary_TXT" FOR READ
WHILE NOT EOF ("Salary_TXT")
    READFILE "Salary_TXT", 
    ############ HELP HERE PLZ
ENDWHILE 
CLOSEFILE "Salary_TXT"
    
    
CASE OF ElementID 
Salary >= 0 and Salary > 25000.0 :ElementID = 0
Salary >= 25000.0 and Salary < 50000.0 :ElementID = 1
Salary >= 50000.0 and Salary < 75000.0  :ElementID = 2
Salary >= 75000.0 and Salary < 75000.0  :ElementID = 3
Salary >= 100000.0 and Salary < 110000.0 :ElementID = 4

OTHERWISE
    ElementID = "INVALID"
ENDCASE

IF gender = "M"
    THEN
        MaleSalary[ElementID] <- MaleSalary[ElementID] + 1
    ELSE
        IF gender = "F"
            THEN
           FemaleSalary[ElementID] <- FemaleSalary[ElementID] + 1

"""