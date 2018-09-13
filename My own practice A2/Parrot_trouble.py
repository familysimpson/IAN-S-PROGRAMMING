
#hour = int(input("Enter hour please"))
talking = False

def parrot_trouble(hour):
    while hour > 23 or hour <0:
        print("Please enter values from 0 to 23")
        hour = int(input("Enter hour again please: "))

    if hour < 7 or hour > 20:
         talking = True
         return talking
         #print(talking, " :parrot is talking")
    else:
        talking = False
        return talking
        #print(talking, " :parrot is not talking")
print(parrot_trouble(5))