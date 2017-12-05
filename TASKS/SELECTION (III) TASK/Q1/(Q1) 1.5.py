#DECLARE TEMPERATURE: INTEGER

print("Enter Temperature")
Temperature = int(input())

if Temperature > 25:
    print("Hot")
elif Temperature >= 20 and Temperature <= 25:
    print("Just Right")
else:
    print("Cold")