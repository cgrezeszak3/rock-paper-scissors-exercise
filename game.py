# this is the "game.py" file...

import random

print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# USER INPUTS
x = input("Please choose either 'rock', 'paper', or 'scissors':")
x = x.lower() 

print("-------------------")

# VALIDATE USER INPUTS
if x not in ["rock","paper","scissors"]:
    print("Invalid input. Please try again")
    quit()

# COMPUTER CHOICE

y = random.choice(["rock","paper","scissors"])

# DISPLAY RESULTS
print("You Chose =", x)
print("Computer Choses =", y)

print("-------------------")

# DETERMINE A WINNER
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

print("-------------------")

print("Thanks for playing. Please play again!")