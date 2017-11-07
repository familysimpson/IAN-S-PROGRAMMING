#messageboard
#declare repeats: INTEGER
#declare counter: INTEGER
#declare message: STRING
message = input("Enter the message to display")
repeats = int(input("Enter the number of times you want the message displayed"))
for counter in range(0,repeats):
    print(message)