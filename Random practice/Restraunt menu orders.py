
SetMenuOption = ["","","","","",""]

SetMenuOption[0] = "Chicken and rice"
SetMenuOption[1] = "Chilli con carne"
SetMenuOption[2] = "Spagetthi meatballs"
SetMenuOption[3] = "Fries"
SetMenuOption[4] = "Rice and brocolli"
SetMenuOption[5] = "Peach and rice"

customer_order = [int,int,int,int,int,int]

customer_order[0] = int
customer_order[1] = int
customer_order[2] = int
customer_order[3] = int
customer_order[4] = int
customer_order[5] = int

Total_customers = 0

no_customers = int(input("How many customers are ordering at one table?"))
print(no_customers,"customers")

for counter in range(0,6):

    print("How many customers ordered:",SetMenuOption[counter])
    customer_order[counter] = int(input("Input number of customers:"))

    Total_customers = Total_customers + customer_order[counter]
    print("Total orders so far:",Total_customers)

    if Total_customers == no_customers:
        print("Thanks for your order")
        break
    if Total_customers >= no_customers:
        print("Too many orders. Start again.")
        break
    else:
        print(customer_order[counter], "orders :", SetMenuOption[counter])

if Total_customers < no_customers:
    print("Too little orders. Start again.")