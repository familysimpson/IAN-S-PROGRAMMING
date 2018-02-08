#DECLARE password: STRING
#DECLARE guess: STRING

password = "BramPT0n"
for counter in range (0,3):
    guess = input("Enter password")
    if guess == password:
        print("Accepted.")
    else:
        print("Wrong. Try again")
print("Logged in")

