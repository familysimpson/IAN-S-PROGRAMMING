#DECLARE InputAge: INTEGER

InputAge = int(input("Please enter your age:"))

if InputAge >= 16  and InputAge <= 21:
    print("You are now eligble for a junior membership")
elif InputAge >21 and InputAge <= 65:
    print("You are now eligible for a standard membership")
elif InputAge > 65:
    print("You are now eligible for a senior membership")
else:
    print("You can only become a member if you are 16 or over 16.")
