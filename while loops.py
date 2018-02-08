#DECLARE password: STRING
#DECLARE guess: STRING

password = "BramPT0n"
attempt = 1
guess = input("Enter password")
while (guess != password) and (attempt < 3):
    if guess == password:
        print("Correct.")
    else:
        print("Incorrect")
        attempt = attempt + 1
        guess = input("Enter password")
if (attempt >= 3) and (guess != password):
    print("Locked")
else:
    print("Logged in")


