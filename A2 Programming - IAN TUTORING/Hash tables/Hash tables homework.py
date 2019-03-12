"""1. In Python create a hashing function that takes in a three letter sequence, and calculates the hash value
using the following formula:
Hash value = sum of ASCII values for each character % (mod) 12.
The hash value should then be returned to the calling function.
"""
charF = input("Enter character")
charM = input("Enter middle character")
charL = input("Enter Last character")

def HashAlgorithm(charF,charM,charL):
    Charactersum = ord(charF) + ord(charM) + ord(charL) #Add up ascii values of characters
    HashValue = Charactersum % 12 #hashing algorithm
    return HashValue

print(HashAlgorithm(charF, charM, charL)) # you just forgot this

#3.The data structure used to hold the three letter sequences is a list named Airport. This list can hold 2000 elements.
#In Python create a procedure to add each three letter sequence to the appropriate index in the list.

#DECLARE Airport: ARRAY [0:1999] OF CHAR
Airport = [""] * 2000
Threelettercharacter = charF,charM,charL

def InsertintoHashTable (ThreeLettercharacter):
    index = HashAlgorithm(Threelettercharacter)
    if Airport[index] == "":
        Airport[index] = ThreeLettercharacter
    else:
        print("ERROR!Hash overflow!")

#PART 2
def InsertintoHashTable (ThreeLettercharacter):
    index = HashAlgorithm(Threelettercharacter) # IAN CAN I DO THIS!?!?!#
    while len(Airport[index]) != 0:
        # find next empty space in array
        index = index + 1
    #Add ThreeLetterhcharacter value to empty array
    Airport[index] = ThreeLettercharacter







