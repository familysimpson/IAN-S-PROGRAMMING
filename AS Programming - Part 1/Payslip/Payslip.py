#payslip
#declare salary : REAL
#declare grosspay : REAL
#declare taxPercent : REAL
#declare netPay : REAL
salary = 35600.0
taxPercent = 20.0
grosspay = salary/12
netPay = grosspay* ((100-taxPercent)/100)
print("Annual salary £",salary)
print("Take home pay each month £",round (netPay,2))