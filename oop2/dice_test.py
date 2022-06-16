#!/usr/bin/python3

# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Multi_Roller

def main():

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    cheater3 = Multi_Roller() # increases number of dice to roll

    # both players take turns
    cheater1.roll()
    cheater2.roll()
    cheater3.roll()

    # both players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()
    cheater3.cheat()

    print(f"Cheater 1 rolled {cheater2.get_dice()}")
    print(f"Cheater 3 rolled {cheater3.get_dice()}")

    if sum(cheater2.get_dice()) == sum(cheater3.get_dice()):
        print("Draw!")

    elif sum(cheater2.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 2 wins!")
    
    else:
        print("Cheater 3 wins!")

if __name__ == "__main__":
    main()