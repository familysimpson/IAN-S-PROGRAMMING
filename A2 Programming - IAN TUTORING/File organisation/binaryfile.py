# code to define a record
class record:
    def __init__(self, firstname, surname, location):
        self.firstname = firstname
        self.surname = surname
        self.location = location

rec1 = record("nicole","carrera","london")
rec2 = record("ian","simpson","stonehaven")
rec3 = record("Deborah","Carrera","Hackney")
rec4 = record("Jamie","Hilder","Germany")

print(rec1.firstname, rec1.surname, rec1.location)

# This is ASCII
ASCII_file = open("testA.txt", "w")
message = "Hello "+rec1.firstname+" "+rec1.surname+". Are you still in "+rec1.location
stonehaven = "Hello "+rec2.firstname+" "+rec2.surname+". Are you still in "+rec2.location
hackney = "Hello "+rec3.firstname+" "+rec3.surname+". Are you still in "+rec3.location
germany = "Hello "+rec4.firstname+" "+rec4.surname+". Are you still in "+rec4.location
ASCII_file.write(message +"\n")
ASCII_file.write(stonehaven +"\n")
ASCII_file.write(hackney+"\n")
ASCII_file.write(germany+"\n")
ASCII_file.close()

# This is Binary
binary_file = open("testB.txt", "wb") # wb not w
binary_message = message.encode('utf8') # these lines just prove the data is in bytes
print(type(binary_message))
print(message)
print(binary_message)

binary_file.write(binary_message) # write bytes to file
binary_file.close()
