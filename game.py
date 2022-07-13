# this is the "game.py" file...

import random

print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# USER INPUTS
player_choice = input("Please choose either 'rock', 'paper', or 'scissors':")
player_choice = player_choice.lower() 
valid_options = ["rock","paper","scissors"]
print("-------------------")

# VALIDATE USER INPUTS
if player_choice not in valid_options:
    print("Invalid input. Please try again")
    quit()

# COMPUTER CHOICE

computer_choice = random.choice(valid_options)

# DISPLAY RESULTS
print("You Chose =", player_choice)
print("Computer Choses =", computer_choice)

print("-------------------")

# DETERMINE A WINNER
if player_choice == "rock" and computer_choice == "rock":
    print("TIE GAME")
elif player_choice == "paper" and computer_choice == "paper":
    print("TIE GAME")
elif player_choice == "scissors" and computer_choice == "scissors":
    print("TIE GAME")
elif player_choice == "rock" and computer_choice == "scissors":
    print("ROCK CRUSHES SCISSORS. YOU WIN!")
elif player_choice == "paper" and computer_choice == "rock":
    print ("PAPER COVERS ROCK. YOU WIN!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("SCISSORS CUT PAPER. YOU WIN!")
elif player_choice == "rock" and computer_choice == "paper":
    print("PAPER COVERS ROCK. COMPUTER WINS :(")
elif player_choice == "scissors" and computer_choice == "rock":
    print("ROCK CRUSHES SCISSORS. COMPUTER WINS :(")
elif player_choice == "paper" and computer_choice == "scissors":
    print("SCISSORS CUT PAPER. COMPUTER WINS :(")
else:
    print("COMBINATION NOT FOUND")

print("-------------------")

print("Thanks for playing. Please play again!")