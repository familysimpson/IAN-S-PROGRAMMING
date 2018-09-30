"""CReate a program that asks the user for a number and then prints
 out a list of all the dividors of that number """

Divs_entry = int(input("Enter a number: "))
DivsEntry = []

for i in range (1,Divs_entry + 1):
    if Divs_entry % i == 0:
        print(i, "is a divisor of ", Divs_entry)
        DivsEntry.append(i)
    else:
        i = i + 1
listlength = len(DivsEntry)
print("There are %d divisors in "%(listlength))

print(DivsEntry)
