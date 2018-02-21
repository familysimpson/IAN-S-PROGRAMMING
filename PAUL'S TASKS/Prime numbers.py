#NC_T4_PRIMES

"""User inputs a number (e.g 20 or 2000)
Program should print on screen all prime numbers less than or equal to that number
(e.g 2,3,5,7,11,13,17,19)
"""

#DECLARE debbie_input : INTEGER
#DECLARE x: INTEGER
#DECLARE y: INTEGER

debbie_input = int(input("Find primes up to what number: "))

for x in range(2, debbie_input + 1):
    isPrime = True
    for y in range(2 , x):
        if x % y == 0:
            isPrime = False
    if isPrime:
        print(x)