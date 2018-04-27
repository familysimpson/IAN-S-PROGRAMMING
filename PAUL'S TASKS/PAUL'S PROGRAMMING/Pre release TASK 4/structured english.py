"""
Name file as Name_Salary_gender_txt

Readline FROM Name_Salary_gender_txt that includes content
UNTIL THERE IS NO content in line from file
CLOSEFILE Name_Salary_gender_txt

CREATE 1D ARRAY Staff_num
ASSIGN Staff_num array EQUALS TO 0 from 0 to 9
//e.g. Staff_num[0] =  0
//     Staff_num[1] =  0
//     Staff_num[2] =  0  etc

SET a = 0
SET b = 0
SET c = 0
SET d = 0
SET e = 0
SET f = 0
SET g = 0
SET h = 0
SET i = 0
SET j = 0

SET Gender_1 = "M"
SET Gender_2 = "F"

SET I = 1 UNTIL IT REACHES THE END OF THE FILE

If line(I) is GREATER THAN 0 or LESS THAN 25000.0 AND Gender_1
    Staff_num [0] = a + 1

ELSE If line(I) GREATER THAN 0 or LESS THAN 25000.0AND Gender_2
    Staff_num [1] = b + 1

ELSE If line(I) GREATER THAN 25000.0 or LESS THAN 50000.0 AND Gender_1
    Staff_num [2] = c + 1

ELSE If line(I) GREATER THAN 25000.0 or LESS THAN 50000.0 AND Gender_2
    Staff_num [3] = d + 1

ELSE If line(I) GREATER THAN 50000.0 or LESS THAN TO 75000.0 AND Gender_1
    Staff_num [4] = e + 1

ELSE If line(I) GREATER THAN 50000.0 or LESS THAN TO 75000.0 AND Gender_2
    Staff_num [5] = f + 1

ELSE If line(I) GREATER THAN 75000.0 or LESS THAN 100000.0 AND Gender_1
    Staff_num [6] = g + 1

ELSE If line(I) GREATER THAN 75000.0 or LESS THAN 100000.0 AND Gender_2
    Staff_num [7] = h + 1

ELSE If line(I) GREATER THAN 100000.0 or LESS THAN or EQUAL TO 110000.0 AND Gender_1
    Staff_num [8] = i + 1

ELSE If line(I) GREATER THAN 100000.0 or LESS THAN or EQUAL TO 110000.0 AND Gender_2
    Staff_num [9] = j + 1


OUTPUT ("The number of employees that are MALE and earn MORE THAN £0.0 AND LESS THAN £25,000.0 is" , Staff_num[0])
OUTPUT ("The number of employees that are FEMALE and earn MORE THAN £0.0 AND LESS THAN £25,000.0 is" , Staff_num[1])

OUTPUT ("The number of employees that are MALE and earn MORE THAN £25,000.0 AND LESS THAN £25,000.0 is" , Staff_num[2])
OUTPUT ("The number of employees that are FEMALE and earn MORE THAN £25,000.0 AND LESS THAN £25,000.0 is" , Staff_num[3])

OUTPUT ("The number of employees that are MALE and earn MORE THAN £50,000.0 AND LESS THAN £25,000.0 is" , Staff_num[4])
OUTPUT ("The number of employees that are FEMALE and earn MORE THAN £50,000.0  AND LESS THAN £25,000.0 is" , Staff_num[5])

OUTPUT ("The number of employees that are MALE and earn MORE THAN £75,000.0  AND LESS THAN £25,000.0 is" , Staff_num[6])
OUTPUT ("The number of employees that are FEMALE and earn MORE THAN £75,000.0  AND LESS THAN £25,000.0 is" , Staff_num[7])

OUTPUT ("The number of employees that are MALE and earn MORE THAN £100,000.0 AND LESS THAN £25,000.0 is" , Staff_num[8])
OUTPUT ("The number of employees that are FEMALE and earn MORE THAN £100,000.0 AND LESS THAN £25,000.0 is" , Staff_num[9])

"""