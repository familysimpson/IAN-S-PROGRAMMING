#DECLARE Number_entry, i : INTEGER

Number_entry = int(input("Enter any number:"))

i = Number_entry

for i in range(0, i+1):
    print(Number_entry,"*", i ,"=", Number_entry * i)
    i = i + 1
    