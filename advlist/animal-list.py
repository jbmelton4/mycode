#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - making selections from complex lists"""

def main():

    #creating an animal list
    list1 = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow", "Hen", "Koi", "Hog", "Jay", "Kit"]

    #display list1
    print(list1)

    #Creating a new list
    list2 = ["Frog", "Weasel", "Lion", "Turkey"]

    #extend list1 by list2
    list1.extend(list2)

    #display new list
    print (list1)

main ()
