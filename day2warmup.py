#!/usr/bin/env python3

def main():

        heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

    # PART 1
    # Print out your favorite character from this list! The output would look something like:
    # My favorite character is Black Panther!

        print(f"My favorite character is {heroes[1]}!") 

    # PART 2
    # Ask the user to pick a number between 1 and 100.
    # Convert the input into an integer.


        nums= int(input("Pick a number between 1 and 100:"))
        print("You said the number is: ",  nums)
        nums= [1, -5, 56, 987, 0]

    # PART 3
    # check out https://docs.python.org/3/library/functions.html or go to Google
    # use a built-in function to find which integer in nums is the biggest.
    # then, print out that number!

        print(f"The biggest number in the hidden list is {max(nums)}!")


    # PART 4
    # put ALL of this code inside a function!
    # look at lab 11, step 4 for an example!


main()
