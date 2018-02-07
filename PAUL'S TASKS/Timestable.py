

print("Here is a times tables grid")
print("Enter the number 12 for a 12 by 12 grid")
answer = int(input())

if answer == 12:
    for no in range(1, 13):
        for no1 in range(1, 13):
            print(no * no1, "", end="")
        print()
    print("End")

