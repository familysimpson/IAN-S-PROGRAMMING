

"""
	DECLARE femaleSalary: ARRAY [0:4] OF INTEGER
	DECLARE maleSalary: ARRAY [0:4] OF INTEGER
	DECLARE Salary: REAL
	DECLARE Gender: CHAR

	DECLARE LINE: STRING
	FemaleSalary[0:4]  0
	MaleSalary[0:4]  0

	OPENFILE "Salary_TXT" FOR READ
	WHILE NOT EOF ("Salary_TXT")
	    READFILE "Salary_TXT", LINE
	    endPos  POS(LINE,‘,’) // POS takes string (line) and looks for 1st char (comma)
	    LINE  RIGHT(LINE, LENGTH(LINE)-endPos)) // removes name from LINE
	    Gender  LEFT(LINE, 1)
	    endPos  POS(LINE,’,’)
	    Salary  RIGHT(LINE, LENGTH(LINE)-endPos))

	    CASE OF ElementID:
	      Salary >= 0 and Salary > 25000.0 :ElementID  0
	      Salary >= 25000.0 and Salary < 50000.0 :ElementID  1
	      Salary >= 50000.0 and Salary < 75000.0  :ElementID  2
	      Salary >= 75000.0 and Salary < 75000.0  :ElementID  3
	      Salary >= 100000.0 and Salary < 110000.0 :ElementID  4

	      OTHERWISE
	        OUTPUT “Error in file. Salary exceeds boundaries”
	    ENDCASE

	    IF gender = "M"
	      THEN
	        MaleSalary[ElementID] <- MaleSalary[ElementID] + 1
	    ELSE IF gender = "F"
	      THEN
	        FemaleSalary[ElementID] <- FemaleSalary[ElementID] + 1
	    END IF


	ENDWHILE
	CLOSEFILE "Salary_TXT"
	OUTPUT ("Here is the number for the female salary", FemaleSalary)
	OUTPUT ("Here is the number for the male salary", MaleSalary)… """
