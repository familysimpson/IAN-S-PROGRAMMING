

Add_member = str(input("Add member:"))
name = str(input("Enter name:"))

while len(str(Add_member))!= 6 :
    print("Membership code invalid. Enter a valid membership code with 6 alphanumeric characters.")
    Add_member = str(input("Add member:"))

print("Here is the valid membership code for:",name,"-",Add_member)


# Ian's attempt

# FOR REFERENCE IF YOU NEED TO MAKE A FUNCTION
# FUNCTION validateMembershipNo(MEMBERID : STRING) RETURNS BOOLEAN
#
# END FUNCTION

# PROCEDURE addNewMember(NAME : STRING, MEMBERID : STRING, CATEGORY : STRING)
#
# END PROCEDURE
def addNewMember(name, memberID, category):
    print

# PROCEDURE printMembershipCard(NAME : STRING, MEMBERID : STRING, CATEGORY : STRING)
#
# END PROCEDURE
def printMembershipCard(name, memberID, category):
    print

# PROCEDURE calculateTotalMembers(MEMBERSJ : ARRAY[1..20,1..2] OF STRING, MEMBERSS : ARRAY[1..20,1..2] OF STRING, MEMBERSSTD : ARRAY[1..20,1..2] OF STRING, NOJUNIORS : INTEGER, NOSENIORS : INTEGER, NOSTANDARDS : INTEGER)
#
# END PROCEDURE
def calculateTotalMembers(membersJ, membersS, membersSTD, noJuniors, noSeniors, noStandards):
    print

# PROCEDURE deleteMember(MEMBERID : STRING, MEMBERSJ : ARRAY[1..20,1..2] OF STRING, MEMBERSS : ARRAY[1..20,1..2] OF STRING, MEMBERSSTD : ARRAY[1..20,1..2] OF STRING)
#
# END PROCEDURE
def deleteMember(memberID, membersJ, membersS, membersSTD):
    print

# main program
# DECLARE name : STRING
# DECLARE memberID : STRING
# DECLARE category : STRING
# DECLARE membersJ : ARRAY[1..20,1..2] OF STRING -- INCREASED THIS FROM STRUCTURE CHART BECAUSE OTHERWISE WOULD NEED TO KNOW RECORDS
# DECLARE membersS : ARRAY[1..20,1..2] OF STRING
# DECLARE membersSTD : ARRAY[1..20,1..2] OF STRING
# DECLARE noJuniors : INTEGER
# DECLARE noSeniors : INTEGER
# DECLARE noStandards : INTEGER
name = ""
memberID = ""
category = ""
noJuniors = 0
noSeniors = 0
noStandards = 0

while True:
    print("Menu: 1 - Add member, 2 - Print card, 3 - Show total members, 4 - Delete member. 0 to quit")
    option = int(input("Enter your choice"))
    while option < 0 or option > 4: # INPUT VALIDATION
        print("Error. Try again.")
        option = int(input("Enter your choice"))
    if option == 1:
        addNewMember(name, memberID, category)
    elif option == 2:
        printMembershipCard(name, memberID, category)
    elif option == 3:
        calculateTotalMembers(members, noJuniors, noSeniors, noStandards)
    elif option == 4:
        deleteMember(memberID, members)
    else:
        exit()

