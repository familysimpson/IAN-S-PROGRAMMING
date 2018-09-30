


Player1 = input("Enter player 1")
Player2 = input ("Enter player 2")

def RockPaperScissors(Player1, Player2):
    if Player1 == Player2:
        print("It's a tie!")
    elif Player1 == "r " and Player2 == "p":
        print("Player 2 won!")
    elif Player1 == "s" and Player2 == "r":
        print ("Player 2 won!")
    elif Player1 == "p" and Player2 == "s":
        print("Player 2 won!")
    else:
        print("Player 1 won!")

RockPaperScissors(Player1,Player2)

replay = input("Would you like to play again")
if replay == "y":
    count = int(input("How may times would you like to play?"))
i = 0
for i in range(count + 1):
    RockPaperScissors(Player1,Player2)
