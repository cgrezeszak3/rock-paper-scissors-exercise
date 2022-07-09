# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")

x = input("Please input your play (rock paper or scissors):")

import random

y = random.choice(["rock","paper","scissors"])

print("My Choice =", x)
print("Computer Choice =", y)

if x == "rock" and y == "rock":
    print("TIE GAME")
elif x == "paper" and y == "paper":
    print("TIE GAME")
elif x == "scissors" and y == "scissors":
    print("TIE GAME")
elif x == "rock" and y == "scissors":
    print("YOU WIN")
elif x == "paper" and y == "rock":
    print ("YOU WIN")
elif x == "scissors" and y == "paper":
    print("YOU WIN")
elif x == "rock" and y == "paper":
    print("COMPUTER WINS")
elif x == "scissors" and y == "rock":
    print("COMPUTER WINS")
elif x == "paper" and y == "scissors":
    print("COMPUTER WINS")
else:
    print("TRY AGAIN")