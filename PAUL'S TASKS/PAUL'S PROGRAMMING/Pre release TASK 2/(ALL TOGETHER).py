#PART 1
#ON PAPER

#PART 2
#Use the structure chart to produce declarations for the modules
# PROCEDURE addNewMember(NAME : STRING, MEMBERID : STRING, CATEGORY : STRING)
#
# END PROCEDURE

# PROCEDURE printMembershipCard(NAME : STRING, MEMBERID : STRING, CATEGORY : STRING)
#
# END PROCEDURE

# PROCEDURE calculateTotalMembers(MEMBERSJ : ARRAY[1:20,1:2] OF STRING, MEMBERSS : ARRAY[1:20,1:2] OF STRING, MEMBERSSTD : ARRAY[1:20,1:2] OF STRING, NOJUNIORS : INTEGER, NOSENIORS : INTEGER, NOSTANDARDS : INTEGER)
#
# END PROCEDURE

# PROCEDURE deleteMember(MEMBERID : STRING, MEMBERSJ : ARRAY[1:20,1:2] OF STRING, MEMBERS : ARRAY[1:20,1:2] OF STRING, MEMBERSSTD : ARRAY[1:20,1:2] OF STRING)
#
# END PROCEDURE

#PART 3
#Convert the pseudocode into program code
def addNewMember(name, memberID, category):
    print

def printMembershipCard(name, memberID, category):
    print

def calculateTotalMembers(membersJ, membersS, membersSTD, noJuniors, noSeniors, noStandards):
    print

def deleteMember(memberID, membersJ, membersS, membersSTD):
    print

#PART 4
#Produce PSEUDOCODE DECLARATIONS second set of modules for the club. The top level module for the reception desk & two lower level modules
    #ENTRY: When member gives a membership code VALIDATE that the code is correct and the member has not already entered. Record the time of entry
    #EXIT: Check the member has entered to exit and record the time of exit

#PROCEDURE validatemembershipcode(MEMBERCODEINPUT : STRING, ENTRYTIME: DATE/TIME)
#
#ENDPROCEDURE

#PROCEDURE Checkmemberexitandrecordtime (MEMBERCODEINPUT: STRING , EXIT_TIME: DATE/TIME)
#
#ENDPROCEDURE