#!/usr/bin/python3

from random import randint
import sys
import time
import os

# time for intro and outro
t1 = 4
t2 = 2
t3 = 6

'''Using Chad's code to get this started!
Warsong, a game where you recruit adventurers as you head towards the goblin lair to defeat them.'''

# Title and start game

print("                                                -----------")
print("                                               |  WARSONG  |")
print("                                                -----------")
print("You must travel to the the ancient fortress to face an evil goblin tribe. You must gather items and recruit adventurers to emerge triumphant!")
print()
startGame = input("Would you like to start your adventure? (Y/N): ").lower
if startGame == 'y' or startGame == 'yes':
    intro()
elif startGame == 'n'or startGame == 'no':
    print("Probably for the best, this thing is prone to crashing.")
    sys.exit()



def intro():
#    print()
 #   time.sleep(t2)
  #  print("You are a loyal retainer of the kingdom, having served many years hunting down and routing vile creatures.")
   # print()
    #time.sleep(t1)
#    print("Having earned the title of Commander, you were assigned to the countryside and have been tasked with eradicating a vicious goblin tribe!")
 #   print()
  #  time.sleep(t1)
   # print("Not the most desirable job for a new Commander but keeping the people safe would earn you favor and fortune with your king.")
 #   print()
  #  time.sleep(t1)
 #   print("Your only companion being a young squire, you set off towards the ancient fortress with an aim to recruit adventurers along the way!")
#    print()
    time.sleep(t3)


# Listing the different party members you can recruit, their health, and certain responses to what happens when issuing COMMAND on them.
party = [{'name' : 'Squire', 'health' : 1},
         {'name' : 'Knight', 'health' : 2},
         {'name' : 'Ranger', 'health' : 2},
         {'name' : 'Cursehunter','health' : 2},
         {'name' : 'Cleric', 'health' : 2}]

# List of monsters
monster = [{'name' : 'Werewolf', 'damage' : 1}]

# Listing the different items
items = [{'name' : 'sprite'},
         {'name' : 'jeweled dagger'}]

# List of abilities
ability = [{'name' : 'rally', 'rally_use' : 1},
         {'name' : 'remove curse'}]


# Player resources.
player_stamina = 5
inventory = []
party = ['squire']
abilities = []
rally_use = 1

# Record of if player gathered all the items, recruited all the heroes, and if the monster was defeated.
def stats():
    print("Something something darkside")

# Instructions for the player.
def showInstructions():
    print('''
TIP #1: Watch your stamina. Maybe there is a way to replenish it...
TIP #2: Command your party members to help you with things. Ask them what you should do next.

--------
Actions:
    GO [north, south, east, west, up, down]
    GET [item, ability]
    USE [item, ability]
    RECRUIT [hero]
    COMMAND [hero]
    LOOK
--------

Type 'help' at any time! Type 'q' to quit!''')

def playerinfo():
#    print('')
#    print('YOU ARE IN THE ' + currentRoom + '.')
    print()
    print('=================================')
    print('Inventory :', str(inventory))
    print('Ability :', str(abilities))
    print('Party :', str(party))
    print('Stamina :', str(player_stamina))
    print('=================================')
    print()


def showStatus(): # display the player's status
 #   if 'desc' in rooms[currentRoom]:
 #   print(rooms[currentRoom]['desc'])
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'] + rooms[currentRoom]['item_status'] + '.')
    if 'ability' in rooms[currentRoom]:
        print('The area around you sparks a memory from your past, ' + rooms[currentRoom]['ability_status'] + '".')
    if 'hero' in rooms[currentRoom]:
        print('You have met a ' + rooms[currentRoom]['hero'].capitalize() + rooms[currentRoom]['hero_status'] + '.')
    if 'monster' in rooms[currentRoom]:
        print('You have encountered a ' + rooms[currentRoom]['monster'].upper() + rooms[currentRoom]['mon_status'] + '!')
#    print('=================')


rooms = {
        'VILLAGE' : {
            'north' : 'GNARLED TREE',
            'west' : 'CENTRAL FOREST',
            'south' : 'WINDMILL',
            'desc' : 'You are in the Village just outside the ancient forest. Homes range from sturdy facilities such as the local inn to thatch-made hovels that serve their purpose. Villagers go about their daily business, oblivious to your noble quest. To the east is the CENTRAL FOREST that beckon you forth. South is the WINDMILL, it\'s arms lazily spinning. To the north you can hear a chilling howl, a GNARLED TREE sitting atop a lonely hill.'
            },

        'WINDMILL' : {
            'north' : 'VILLAGE',
            'west' : 'SOUTH FOREST',
            'down' : 'BASEMENT',
            'desc' : 'You have arrived at the old windmill. Its sails look a bit worse for wear but the stone work seems sturdy despite the recent goblin attacks. You swear it looked like a giant as you approached...',
            'hero' : 'knight',
            'hero_status' : '! Their armor looks ancient and worn as you watch them practice their swordplay. They stop for a moment, their weathered face regards you with a raised brow and a kindly nod',
            },

        'SWAMP' : {
            'east' : 'SOUTH FOREST',
            'north' : 'PEACEFUL GLADE', # You need the crytal flower to go here
            'desc' : 'You are in the foul smelling swamp. Twisting roots and buzzing insect abound. There are several goblin corpses with arrows jutting out of their corpses. A large worg is face down in the murky water, its back riddled with arrows. You feel a warm, welcoming sensation pulling you to the north but don\'t see a path. Back to the east lies the southern forest.',
            'hero' : 'ranger',
            'hero_status' : '! They are going about restringing their bow. They offer a stern stare with piercing eyes, possibly wondering why you are all the way out here',
            },

        'GNARLED TREE' : {
            'west' : 'NORTH FOREST',
            'south' : 'VILLAGE',
            'desc' : 'A twisted tree, sinister and dying reaches towards the sky like a skeletal hand risen from the grave. This is a cursed place, the hair on the back of your neck is on end as you feel you stomach sink.',
            'monster' : 'werewolf',
            'mon_status' : '! It glares at you with bright red eyes, snarling!',
            },
        
        'CENTRAL FOREST' : {
            'south' : 'SOUTH FOREST',
            'north' : 'NORTH FOREST',
            'east' : 'VILLAGE',
            'desc' : 'You are in the center of the forest. A sinister looking warrior with a wide brimmed hat and a silver sword looks at you and nods solemnly. North is lies more forest as far as you can tell. South lies a hill that let\'s you overlook the forest. East takes you back to the village.',
            'hero' : 'cursehunter',
            'hero_status' : '! They are sharpening a silver sword, a solemn look on their face as they look in the direction of the hair-raising howl',
            },

        'SOUTH FOREST' : {
            'north' : 'CENTRAL FOREST',
            'west' : 'SWAMP',
            'east' : 'WINDMILL',
            'desc' : 'You are in the southern forest, standing atop a hill that gives you a view above the treeline. Further west lies a swamp and heading north seems to reveal even more forest than you anticipated. Heading east will bring you to the old windmill.',
            'ability' : 'rally',
            'ability_status' : 'reminding you of a time you had to -RALLY- the troops!',
            'item' : 'sprite',
            'item_status' : ' shimmering beneath a mossy log but it looks difficult to move by yourself',
            },

        'PEACEFUL GLADE' : {
            'south' : 'SWAMP',
            'east' : 'NORTH FOREST',
            'desc' : 'You are in a serene glade, a babbling brook can be heard as the smell of the swamp is left behind and a scent of flowers hangs in the air. Small glowing sprites dart around, curious of your presence.',
            },

        'NORTH FOREST' : {
            'south' : 'CENTRAL FOREST',
            'east' : 'GNARLED TREE',
            'west' : 'PEACEFUL GLADE', # You need the sprite or the jeweled dagger to enter from this direction.
            'desc' : 'The north forest is pretty quiet, you get a sense of being watched but you don\'t feel threatened by it. You sense a warm, peaceful sensation pulling you to the west but see no path ahead. To the east lay the gnarled tree, howling still echoing in the distance. South leads you to the center of the forest.' 
            }
        }

currentRoom = 'VILLAGE'   # player start location

os.system('clear') # start game with a fresh screen
intro() # kinda gives the starting background
showInstructions()     # show instructions to the player

while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()

    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('>>') # so long as the move does not
                           # have a value. Ask the user for input

    move = move.lower().split() # make everything lower case because directions and items require it, then split into a list
    os.system('clear') # clear the screen
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc'])

            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")

####### WEREWOLF FIGHT


# Commands [Recruit, Command, Go, Get, Use, Look]
    if move[0] == 'recruit':
        if 'hero' in rooms[currentRoom] and move[1] in rooms[currentRoom]['hero']:
            party += [move[1]] # add hero to party
            print('The ' + move[1].capitalize() + ' has decided to join you!') # msg saying you received the item
            del rooms[currentRoom]['hero'] # deletes that hero from the dictionary

    # Using the heroes. Need to figure out how to use them as "keys".
    if move [0] == 'command':
        if move[1].lower() == 'squire' in party:
            print()
        if move[1].lower() == 'knight' in party:
            print()
        if move[1].lower() == 'ranger' in party:
            print()
        if move[1].lower() == 'cursehunter' in party:
            print()
        if move[1].lower() == 'cleric' in party:
            print()

    if move[0] == 'use':
        #### RALLY
        if move[1].lower() == 'rally' in abilities:
            print("You rally those around you, feeling a strong desire to push on!")
            player_stamina += 2
            rally_use -= 1
        elif rally_use == 0:
            player_stamina +=0
            print("You feel you cannot rally the troops again today.")
        if move[1].lower() == 'rally' not in abilities:
            print("That sounds familiar to you but you can\' quite remember.")  

        #### REMOVE CURSE
        if move[1].lower() == 'remove curse' in abilities:
            print("You recite the magic words given to you by the Fairy Queen! They fade from your memory as soon as you speak them!")
            del abilities['remove curse']

    if move[0] == 'go':
        player_stamina -=1

    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]] # add item to inv
            print(move[1].capitalize() + ' received!') # msg saying you received the item
            del rooms[currentRoom]['item'] # deletes that item from the dictionary
        elif 'ability' in rooms[currentRoom] and move[1] in rooms[currentRoom]['ability']:
                abilities += [move[1]]  # add ability to abilities
                del rooms[currentRoom]['ability']

        else:
            print('Seems you can\'t travel in that direction ' + (move[1].upper()) + '.')

    if move[0] == 'look':
        if 'desc' in rooms[currentRoom]:
            print(rooms[currentRoom]['desc']) # print the look description
        else:
            print('You can\'t see a damn thing for some reason.')
    

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in player_stamina >= 0:
        print('\n"You have done all you could for today and head to the village inn. You feel your journey has only just begun."')
        print("Would you like to quit [Y/N] or view your final statistics [STATS]? ")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        if quit_query.lower() in ['stats']:
            stats()
        else:
            intro()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass