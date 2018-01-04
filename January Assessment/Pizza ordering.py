#Pizza ordering #Nicole Carrera #04/01/18

order = ""
orderNo = 1
Base = ""
Choice = ""
Again = ""
TopCount = 0
Index = 0
ShopOpen = True
EndOrder = False

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

print("Would you like a THIN or THICK pizza base?")
THIN = "THIN" or "thin" or "Thin"
THICK = "THICK" or "thick" or "Thick"
input("Enter THIN or THICK")
print("Your order number is",orderNo)

print("Enter a topping from the list and how many toppings you would like")
Topping = input(TopName[0:9])
input = TopName[0:9]
