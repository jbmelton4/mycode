#!/usr/bin/env python3
import random

#GOALS
# python will choose a number between 1 and 100
# user will make a guess
# if the user guesses too high, they'll be told "high"
# too low, be told "too low"
# 10 guesses to get the answer right

num = random.randint(1,100)
turn= 0

print("DEBUG:", num)

while turn < 10:

    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess.isdigit():
        guess= int(guess)

    else:
        print("That is not a proper number!")
        continue

    turn += 1
    
    # check if guess is too high
    if guess > num:
        print("Too high!")

    elif guess < num:
        print("Too low!")

    else: 
        print("Correct! The answer was", num)
        break

    if turn == 10:
        print("You had too many incorrect guesses. The correct answer was ", num)
        break

    
