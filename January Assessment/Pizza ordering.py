#Pizza ordering #Nicole Carrera #04/01/18

#DECLARE order: STRING
#DECLARE orderNo: INTEGER
#DECLARE base : STRING
#DECLARE choice: STRING
#DECLARE again: STRING
#DECLARE TopCount: INTEGER
#DECLARE index: INTEGER
#DECLARE ShopOpen: BOOLEAN
#DECLARE EndOrder: BOOLEAN

#DECLARE TopName: ARRAY[0:9] OF STRING
TopName = ["","","","","","","","","",""]

TopName[0] = "Cheese"
TopName[1] = "Ham"
TopName[2] = "Pepperoni"
TopName[3] = "Pineapple"
TopName[4] = "Mushroom"
TopName[5] = "Cherry tomatoes"
TopName[6] = "Chicken"
TopName[7] = "Peppers"
TopName[8] = "Olives"
TopName[9] = "Jalapenos"

# DECLARE TopAmnt: ARRAY[0:9] OF INTEGER
TopAmnt = [10,10,10,10,10,10,10,10,10,10]

print(0, TopName[0], TopAmnt[0])
print(1, TopName[1], TopAmnt[1])
print(2, TopName[2], TopAmnt[2])
print(3, TopName[3], TopAmnt[3])
print(4, TopName[4], TopAmnt[4])
print(5, TopName[5], TopAmnt[5])
print(6, TopName[6], TopAmnt[6])
print(7, TopName[7], TopAmnt[7])
print(8, TopName[8], TopAmnt[8])
print(9, TopName[9], TopAmnt[9])

orderNo = 1

order = "Order no " + str(orderNo) + ': '
base = input("Enter your choice of base (T)hin or (P)an: ")
while base.upper() != "T" and base.upper() != "P":
    print("Not a valid base type. Try again.")
    base = input("Enter your choice of base (T)hin or (P)an: ")

if base.upper() == "T":
    order = order + "Thin base. "
else:
    order = order + "Pan base. "

endOrder = False
topCount = 0
choice = int(input("Enter topping number (0-9): "))

while choice < 0 or choice > 9:
    print("Not a valid topping choice. Try again.")
    choice = int(input("Enter topping number (0-9): "))
order = order + TopName[choice] + ". "
print(order)

again = str(input("Would you like another topping? Yes or No"))
while again == "Yes" or "No"
    