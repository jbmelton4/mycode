#!/usr/bin/env python3
"""Week 2 Morning Warmup"""
def main():

    words= ["astonishing", "disgusting", "damaging", "dreadful", "amazing", "awesome", "astounding", "distressing"]

# OBJECTIVE 1: break the while loop when the user ACTUALLY types something in
    while True:
        name= input("What is your name?\n>")
        if name != "":
                break

    with open("monday.txt", "w") as fileobj:
        for x in words:
            if x.startswith("a"):
                fileobj.write(f"Hello, {name}! I hope you have an {x} day today!\n")

    # NOTE: there are four a-words, so there should be four lines of output in the "monday.txt" file!

    # OBJ. 2: put the correct permission argument in the open() function below
        # OBJ. 3- while indented under the with/as, loop over the "words" list above
        # OBJ. 4- add if logic to only allow words that start with the letter "a"
        # OBJ. 5- insert "name" and each "a-word" into the .write() line below.
        
    # OBJ. 6- put all this code inside a function :)

main()