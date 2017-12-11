#JANUARY ASSESSMENT PREPARATION  #GUESSINGGAME #NICOLE_CARRERA #07/12/17

print("Enter the four names of the team")
Four_names_of_teams = ["","","",""]

Four_names_of_teams[0] = input("Enter team 1")
Four_names_of_teams[1] = input("Enter team 2")
Four_names_of_teams[2] = input("Enter team 3")
Four_names_of_teams[3] = input("Enter team 4")

import random
Four_names_of_team1 = random.choice(Four_names_of_teams)
Four_names_of_team2 = random.choice(Four_names_of_teams)
print(Four_names_of_team1)
print(Four_names_of_team2)

Answer1 = random.randint(1,10)
print(Four_names_of_team1,"Enter a number")
number = int(input())
while number != Answer1:
        print("Enter another number")
        number = int(input())
print("Correct number!")

Answer2 = random.randint(1,10)
print("Enter a number")
number = int(input())
while number != Answer2:
        print(Four_names_of_team2,"Enter another number")
        number = int(input())
print("Correct number!")


