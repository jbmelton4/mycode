import random

# Rando words to use
wordbank= ["four", "spaces"]

# TLG student list, sorted by numbers 0-17
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

random.shuffle(tlgstudents)

num= int(input("Pick a number:"))


print(f"{tlgstudents[num]} always uses {wordbank[0]} {wordbank[1]} to indent.")



