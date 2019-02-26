"""1. In Python create a hashing function that takes in a three letter sequence,
 and calculates the hash value using the following formula:
Hash value = sum of ASCII values for each character % (mod) 12
The hash value should then be returned to the calling function.
"""


charF = input("Enter character")
charM = input("Enter middle character")
charL = input("Enter Last character")

def Hash(charF,charM,charL):
    Charactersum = ord(charF) + ord(charM) + ord(charL)
    HashValue = Charactersum % 12
    return HashValue






