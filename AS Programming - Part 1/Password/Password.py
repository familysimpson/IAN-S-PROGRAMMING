#password
#declare noAttempts : INTEGER
#declare password : STRING
#declare attempt : STRING
password = "davinci"
for noAttempts in range(1,4):
    attempt = input("Enter password:")
    if password == attempt:
        print("Password correct")
        break
    else:
        print("Incorrect. Try again.")
