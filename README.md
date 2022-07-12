# rock-paper-scissors-exercise

## Environment Setup
When opening the code for the first time only, create a new conda environment by using the below command on the command line

conda -n my-gam-env python=3.8

This command will create the new environment and install python 3.8 as the python version for the python files in the environment to run off of

Once the environment is created or if this is not the first time opening the code file, use the command

conda activate my-game-env

to activate the new environment that you just created.

Then, run the python file by using the command

python game.py

## Game Play
When prompted by the game, enter in your pla, which can be either rock, paper, or scissors and then hit enter.

## Game Results
If your play input was a valid option for the game, the game will display your choice, the computer's choice, and which player won the game.

## Invalid Entries
If you enter in a value that is not rock, paper, or scissors, the game will fail due to an invalid input. You will see a message of "Invalid input. Please try again" displayed. 