
Add_member = str(input("Add member:"))
name = str(input("Enter name:"))

while len(str(Add_member))!= 6 :
    print("Membership code invalid. Enter a valid membership code with 6 alphanumeric characters.")
    Add_member = str(input("Add member:"))

print("Here is the valid membership code for:",name,"-",Add_member)


# FOR REFERENCE IF YOU NEED TO MAKE A FUNCTION
# FUNCTION validateMembershipNo(MEMBERID : STRING) RETURNS BOOLEAN
#
# END FUNCTION


Board = [[final for r in range(1)] for j in range(1)]
print(Board)