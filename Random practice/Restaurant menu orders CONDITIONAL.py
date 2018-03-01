
SetMenuOption = ["","","","","",""]

SetMenuOption[0] = "Pumpkin soup"
SetMenuOption[1] = "Cow foot & rice'n'peas"
SetMenuOption[2] = "Jerk chicken"
SetMenuOption[3] = "Plantain fries"
SetMenuOption[4] = "Ackee & Salfish"
SetMenuOption[5] = "Curry goat & lamb"

customer_order = [0,0,0,0,0,0]

Total_customers = 0

no_customers = int(input("How many customers are ordering at one table?"))
print(no_customers,"customers")

counter = 0
while no_customers > Total_customers:

    print("How many customers ordered:",SetMenuOption[counter])
    customer_order[counter] = int(input("Input number of customers:"))
    while customer_order[counter] < 0 or customer_order[counter] > (no_customers - Total_customers):
        print("Too many orders. Try again.")
        print("How many customers ordered:", SetMenuOption[counter])
        customer_order[counter] = int(input("Input number of customers:"))

    Total_customers = Total_customers + customer_order[counter]
    print("Total orders so far:",Total_customers)


    counter += 1

print("Thanks for your order")

for counter in range(0,6):
    print(customer_order[counter], "orders :", SetMenuOption[counter])