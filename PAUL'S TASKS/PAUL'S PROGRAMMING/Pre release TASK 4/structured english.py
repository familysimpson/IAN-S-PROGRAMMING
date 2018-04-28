"""
CREATE 1D ARRAY femaleSalary
ASSIGN femaleSalary array EQUALS TO 0 from 0 to 4
//e.g. femaleSalary[0] =  0
//     femaleSalary[1] =  0
//     femaleSalary[2] =  0  etc

CREATE 1D ARRAY maleSalary
ASSIGN maleSalary array EQUALS TO 0 from 0 to 4

OPEN Name_Salary_gender_txt for READ
Readline FROM Name_Salary_gender_txt that includes content INTO line
UNTIL THERE IS NO content in line from file

EXTRACT gender FROM line
EXTRACT salary FROM line

If salary is GREATER THAN OR EQUAL TO 0 or LESS THAN OR EQUAL TO 25000.0
    SET elementID = 0

ELSE If salary GREATER THAN 25000.0 or LESS THAN OR EQUAL TO 50000.0
    SET elementID = 1

ELSE If salary GREATER THAN 50000.0 or LESS THAN OR EQUAL TO 75000.0
    SET elementID = 2

ELSE If salary GREATER THAN 75000.0 or LESS THAN OR EQUAL TO 100000.0
    SET elementID = 3

ELSE If salary GREATER THAN 100000.0 or LESS THAN or EQUAL TO 110000.0
    SET elementID = 4

IF gender is EQUAL TO "F"
    INCREMENT femaleSalary array ELEMENT elementID BY 1
    // e.g. femaleSalary[0] = femaleSalary[0] + 1

ELSE IF gender is EQUAL to "M"
    INCREMENT maleSalary array ELEMENT elementID BY 1

CLOSEFILE Name_Salary_gender_txt

//The salary wages are going from highest to lowest in the array
//IF NEEDED
//OUTPUT ("Here is the number for the female salary" ,femaleSalary)
//OUTPUT ("Here is the number for the male salary " ,maleSalary)



"""