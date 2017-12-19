#JANUARY ASSESSMENT PREPARATION  #GUESSINGGAME #NICOLE_CARRERA #07/12/17

#DECLARE Four_names_of_teams: [0..4] OF ARRAY OF STRING

import random
print("Enter the four names of the team")
Four_names_of_teams = ["","","",""]

Four_names_of_teams[0] = input("Enter team 1")
Four_names_of_teams[1] = input("Enter team 2")
Four_names_of_teams[2] = input("Enter team 3")
Four_names_of_teams[3] = input("Enter team 4")

Four_names_of_team1 = random.choice(Four_names_of_teams)
Four_names_of_team2 = random.choice(Four_names_of_teams)
print(Four_names_of_team1)
print(Four_names_of_team2)

noAttempts1 = 0
guess1 = -1

noAttempts2 = 0
guess2 = -1

Answer1 = random.randint(1,10)
print(Four_names_of_team1,"Enter a number from 1 to 10")
number = int(input())
while number != Answer1:
        print("Enter another number")
        number = int(input())
        noAttempts1 += 1
print("Correct number!")
print("Player 1 ;here is your number of attempts taken:", noAttempts1)

Answer2 = random.randint(1,10)
print(Four_names_of_team2,"Enter a number from 1 to 10")
number = int(input())
while number != Answer2:
        print(Four_names_of_team2,"Enter another number")
        number = int(input())
        noAttempts2 += 1
print("Correct number!")
print("Player 2; here is your number of attempts taken:",noAttempts2)

if noAttempts1 > noAttempts2:
        print("Player 1 is the winner!")
elif noAttempts2 > noAttempts1:
        print("Player 2 is the Winner!")
elif noAttempts1== noAttempts2:
        print("It's a draw!")


REPEAT1 = print(Four_names_of_team1,"Would you like to play again? YES OR NO")
while REPEAT1 != "quit":
        Four_names_of_team1.clear()
        noAttempts1.clear()

REPEAT2 = print(Four_names_of_team2,"Would you like to play again? YES OR NO")
while REPEAT1 != "quit":
        Four_names_of_team2.clear()
        noAttempts1.clear()