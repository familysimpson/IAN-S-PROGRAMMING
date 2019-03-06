import random

k = random.uniform(-10.0,10.0)
floatingArray = [""] * 1000
floatingrandom = open("RandomFloatingnumbers.txt","w")
floatingrandombinary = open("RandomFlaotingNumbersTEST2.txt","wb")
for p in range(0,1000):
    floatingArray[p] = k
    k = random.uniform(-10.0,10.0)
    Randomnumbers = str(floatingArray[p]) + "," + "\n"
    binaryRandomnumbers = (Randomnumbers).encode("utf8")
    floatingrandombinary.write(binaryRandomnumbers)
    floatingrandom.write(Randomnumbers)
floatingrandom.close
floatingrandombinary.close




