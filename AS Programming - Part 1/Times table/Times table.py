#times table
#declare counter: INTEGER
#declare number: INTEGER
#declare sum: INTEGER
number = int(input("Enter a number:"))
for counter in range(1,13):
    sum = number*counter
    print(counter,"x",number,"=",sum)