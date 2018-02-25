
SetMenuOption = ["","","","","",""]

SetMenuOption[0] = "Chicken and rice"
SetMenuOption[1] = "Chilli con carne"
SetMenuOption[2] = "Spagetthi meatballs"
SetMenuOption[3] = "Fries"
SetMenuOption[4] = "Rice and brocolli"
SetMenuOption[5] = "Peach and rice"

order = [int,int,int,int,int,int]

order[0] = int(input())
order[1] = int(input())
order[2] = int(input())
order[3] = int(input())
order[4] = int(input())
order[5] = int(input())

nocustomers = int(input("How many customers are ordering at one table?"))
print(nocustomers)

print("How many customers want",SetMenuOption[0])