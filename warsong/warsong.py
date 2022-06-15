#!/usr/bin/python3

from random import randint
import sys
import time
import os
import os.path
import textwrap
import crayons

screen_width = 100

# Times (seconds)
t1 = 1
t2 = 3
t3 = 6

# Record of if player gathered all the items/abilities, recruited all the heroes, and if the monster was defeated.
# !!!!! Doesn't like this, gotta figure out a way to add to this. Maybe look up something about 'increasing scores'?
#def stat_tracker():
#    stat_trackerH = 1 # Shows how many heroes you've recruited
#    stat_trackerA = 0 # Shows how many abilities you've unlocked
#    stat_trackerI = 0 # Shows how many items you've received
#    boss_defeated = 0 # Shows if you've defeated the boss
#    print("Something something darkside")

#### Save Function ####
# !!!!! Not working as intended. I'll try putting a load game function into the START GAME prompt instead. Doesn't work as intended anyways, dang.
def save():
    list = [
                player_stamina,
                inventory,
                party,
                abilities, 
                rally_use
            ]
    f = open("load_game.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close

##### Main Menu #####
# !!!!! Broken. Skips straight to the START GAME bit. Hmmmm....I should figure out how to merge the two instead of making multiple menus, that's annoying.
#def mainMenu():
    os.system('clear')
    while mainMenu:
        print('''  
        
                                ( W A R S O N G )  
                    -------------------------------------
                    |             MAIN MENU             |
                    |                                   |
                    |             NEW GAME              |
                    |             LOAD GAME             |
                    |             QUIT GAME             |
                    |                                   |
                    ------------------------------------- ''')
                
        choice = input("> ").lower

        if choice == "new game" or "new":
            intro()

        elif choice == "load game" or "load":
            f = open("load_game.txt", "r")
            load_list = f.readline()
            player_stamina = [0][:-1]
            inventory = [1][:-1]
            party = [2][:-1]
            abilities = [3][:-1]
            rally_use = [4][:-1]
            print(player_stamina, inventory, party, abilities, rally_use)
            print("Welcome back, Commander!")
            warsong()

        elif choice == "quit":
            sys.exit()

def warsong():
    os.system('clear')
    '''Warsong, a game where you recruit adventurers as you head towards the goblin lair to defeat them.'''

    #### GAME INTRO ####
    def intro():
    #   print()
    #   time.sleep(t2)
    #   print("You are a loyal retainer of the kingdom, having served many years hunting down and routing vile creatures.")
    #   print()
    #   time.sleep(t1)
    #   print("Having earned the title of Commander, you were assigned to the countryside and have been tasked with eradicating a vicious goblin tribe!")
    #   print()
    #   time.sleep(t1)
    #   print("Not the most desirable job for a new Commander but keeping the people safe would earn you favor and fortune with your king.")
    #   print()
    #   time.sleep(t1)
    #   print("Your only companion being a young squire, you set off towards the ancient fortress with an aim to recruit adventurers along the way!")
    #   print()
       time.sleep(t1)


                                                    #### Title and Start Game ####

    print("                                                -----------"     )
    print("                                               |  WARSONG  |"    )
    print("                                                -----------"     )
    print("You must travel to the the ancient fortress to face an evil goblin tribe. You must gather items and recruit adventurers to emerge triumphant!\n")
    print()
  
    # Start Game
    startGame = input("Would you like to start your adventure? (Y/N): \n").lower()
    if startGame == 'y' or startGame == 'yes':
        intro()
    else:
        print("Probably for the best, the journey is only for the brave and heroic.\n")
        sys.exit()


     # Listing the different party members you can recruit, their health, and certain responses to what happens when issuing COMMAND on them.
    party = [
            {'name' : 'Squire', 'health' : 1},
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

    #### Player Resources ####
    player_stamina = 5
    inventory = []
    party = ['squire']
    abilities = []
    rally_use = 1

    # Instructions for the player.
    def showInstructions():
        print('''
    TIP #1: Watch your stamina. Maybe there is a way to replenish it...
    TIP #2: Command your party members to help you with things. Ask them what you should do next.

    -------------------------------------
    |             Actions:              |
    |    GO [north, south, east, west]  |
    |    GET [item, ability]            |
    |    USE [item, ability]            |
    |    RECRUIT [hero]                 |
    |    COMMAND [hero]                 |
    |    LOOK                           |
    -------------------------------------
    Type 'help' at any time! Type 'q' to quit! ''')

    def playerinfo():
        #print('')
        #print('YOU ARE IN THE ' + currentRoom + '.')
        print()
        print('=================================')
        print('Inventory :', str(inventory))
        print('Ability :', str(abilities))
        print('Party :', str(party))
        print('Stamina :', str(player_stamina))
        print('=================================')
        print()


    def showStatus(): 
    # display the player's status
    # if 'desc' in rooms[currentRoom]:
    # print(rooms[currentRoom]['desc'])
        
        if 'item' in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'] + rooms[currentRoom]['item_status'] + '.\n')
        if 'ability' in rooms[currentRoom]:
            print('The area around you sparks a memory from your past, ' + rooms[currentRoom]['ability_status'] + '.\n')
        if 'hero' in rooms[currentRoom]:
            print('You have met a ' + rooms[currentRoom]['hero'].capitalize() + rooms[currentRoom]['hero_status'] + '.\n')
        if 'monster' in rooms[currentRoom]:
            print('You have encountered a ' + rooms[currentRoom]['monster'].upper() + rooms[currentRoom]['mon_status'] + '!\n')
        #print('=================')


    rooms = {
            'VILLAGE' : {
                'north' : 'GNARLED TREE',
                'west' : 'CENTRAL FOREST',
                'south' : 'WINDMILL',
                'desc' : 'You are in the Village just outside the ancient forest. Buildings range from sturdy facilities such as the local inn to thatch-made hovels that serve their purpose. Half of the homes seem to have been burned down, no thanks to a recent goblin raid. People go about trying to get their village back to normal, oblivious to your noble quest. To the east is the center of the forest that beckon you forth. South is an old windmill, it\'s arms lazily spinning. To the north you can hear a chilling howl, a gnarled tree sitting atop a lonely hill.'
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
                # Need to use the sprite to gain access to the north, the PEACEFUL GLADE 
                'desc' : 'You are in the foul smelling swamp. Twisting roots and buzzing insect abound. There are several goblin corpses with arrows jutting out of their corpses. A large worg is face down in the murky water, its back riddled with arrows. You feel a warm, welcoming sensation pulling you to the north but don\'t see a path. Back to the east lies the southern forest.',
                'hero' : 'ranger',
                'hero_status' : '! They are going about restringing their bow. They offer a stern stare with piercing eyes, possibly wondering why you are all the way out here',
                },

            'GNARLED TREE' : {
                'west' : 'NORTH FOREST',
                'south' : 'VILLAGE',
                'desc' : 'A twisted tree, sinister and dying reaches towards the sky like a skeletal hand risen from the grave. This is a cursed place, the hair on the back of your neck is on end as you feel your stomach sink.',
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
                'item_status' : ' shimmering beneath a mossy log. It seems stuck but it looks difficult to move the log by yourself',
                },

            'PEACEFUL GLADE' : {
                'south' : 'SWAMP',
                'east' : 'NORTH FOREST',
                'desc' : 'You are in a serene glade, a babbling brook can be heard as the smell of the swamp is left behind and a scent of flowers hangs in the air. Small glowing sprites dart around, curious of your presence.',
                },

            'NORTH FOREST' : {
                'south' : 'CENTRAL FOREST',
                'east' : 'GNARLED TREE',
                # Need the jeweled dagger to head west to the PEACEFUL GLADE
                'desc' : 'The north forest is pretty quiet, you get a sense of being watched but you don\'t feel threatened by it. You sense a warm, peaceful sensation pulling you to the west but see no path ahead. To the east lay the gnarled tree, howling still echoing in the distance. South leads you to the center of the forest.' 
                }
            }

    currentRoom = 'VILLAGE'   # player start location
        

    os.system('clear') # start game with a fresh screen
    intro() # kinda gives the starting background
    showInstructions()  # show instructions to the player

    while True:   # MAIN INFINITE LOOP
        #### Player Stamina ---> End Game       
        if player_stamina <= -1:
            os.system("clear")
            print('\nExhausted, you feel have done all you could for today and head to the village inn. You wonder if you should press on ahead in the morning or abandon your quest...\n')
            print("Would you like to quit [Q]? View your final statistics [STATS]? Or move on to the next chapter? [ONWARD]\n")
            quit_query = input('>')
            if quit_query.lower() in ['q', 'quit']:
                print("Thanks for playing!\n")
                sys.exit()
            if quit_query.lower() in ['onward']:
                sys.exit()
            if quit_query.lower() in ['stats']:
                stat_tracker() #Show how many items/heroes were collected and if werewolf was defeated.
            else:
                warsong() # I think this restarts the game

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
                player_stamina -= 1
                if 'desc' in rooms[currentRoom]:
                    print(rooms[currentRoom]['desc'])

                # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
            else:
                print("You can't travel in that direction.")

    #### WEREWOLF FIGHT

        # If your party is empty, the werewolf kills you. Game over.
        # If you command your squire, the werewolf kills your squire and temporarily leaves. A noble sacrifice? The jeweled dagger should be on the ground. If you go back, the werewolf will appear again.
        # If you command your knight/ranger, they take (1) damage untill their health is (0/2). They can die and are removed from your party. The werewolf is in a frenzy after killing one of them and kills you next. Game over.
        # >> A message will print from them after initial attack, insisting to press the attack, kind of tricking you into commanding them again and resulting in a Game Over.
        # If you command your cursehunter, they kill the werewolf. The cursehunter then leaves your party. Boss = dead
        # If you use 'remove curse', the werewolf is cured and becomes a cleric that is instantly added to your party. Boss = dead


    #### Commands [Recruit, Command, Go, Get, Use, Look, Super Secret Commands]
        # !!!! Trying to make it to where using wrong command on them triggers an invalid response. Need to do the same for use on something not in your inventory.
        if move[0] == 'recruit':
            if 'hero' in rooms[currentRoom] and move[1] in rooms[currentRoom]['hero']:
                party += [move[1]] # add hero to party
                print(crayons.cyan('\nThe ' + move[1].capitalize() + ' has decided to join you!\n', bold=True)) # msg saying you received the hero
                #stat_trackerH += 1 # Adds to the stat tracker
                del rooms[currentRoom]['hero'] # deletes that hero from the dictionary
            else:
                print('The ' + move[1].capitalize() + ' seems annoyed you would try such a thing.')

        # Using the heroes. Need to figure out how to use them as "keys". Take a look at sprite.
        if move[0] == 'command':
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

        # Using items in your inventory.
        if move[0] == 'use':

            #### SPRITE ####
            # Sprite is needed to gain access to PEACEFUL GLADE from SWAMP
            if move[1].lower() == 'sprite' and currentRoom == 'SWAMP' and 'sprite' in inventory:
                print(crayons.blue("The sprite shines a bright blue hue, beckoning you to follow it! A path opens up to the north...", bold=True))
                rooms["SWAMP"]["north"] = "PEACEFUL GLADE"
                inventory.remove ('sprite')

            #### Jeweled Dagger ####
            # The dagger is needed to gain access to PEACEFUL GLADE from NORTH FOREST. 
            if move[1].lower() == 'sprite' and currentRoom == 'NORTH FOREST' and 'jeweled dagger' in inventory:
                print(crayons.blue("A brilliant light pierces through the dark forest, slamming into the dagger and lighting it on fire! Dropping the melted weapon, you swear you saw a sinister visage of a skull in the smoke! A path opens up to the west.", bold=True))
                rooms["NORTH FOREST"]["west"] = "PEACEFUL GLADE"
                inventory.remove ('jeweled dagger')

            #### RALLY ####
            # !!! Need to make it to where you can only use it once. Look at move and how we got that to stop draining stamina for wrong directions.
            if move[1].lower() == 'rally' in abilities:
                player_stamina += 2
                rally_use -= 1
                print(crayons.green("You rally those around you, feeling a strong desire to push on!", bold=True))
            if move[1].lower() == 'rally' not in abilities:
                print("That sounds familiar to you but the memory escapes you, just out of reach.")
            elif move[1].lower() == rally_use == 0: 
                print(crayons.red("You feel you cannot rally the troops again today.", bold=True)) 

            #### REMOVE CURSE  ####
            # ******* A secret ability. You need to use the ranger or cursehunter to convince the fairy queen to give you the ability.
            # ******* Using it on the werewolf triggers the end of the scenario, triggering a 'cutscene' and adds the cleric to your party.
            if move[1].lower() == 'remove curse' in abilities:
                print(crayons.green("You recite the magic words given to you by the Fairy Queen! They fade from your memory as soon as you speak them!", bold=True))
                del abilities['remove curse']

        # Acquiring items and abilities.
        if move[0] == 'get':
            if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                inventory += [move[1]] # add item to inv
                print(crayons.yellow('\nYou have received the ' + move[1].capitalize() + '!\n', bold=True)) # msg saying you received the item
                #stat_trackerI += 1 # Adds to the stat tracker
                del rooms[currentRoom]['item'] # deletes that item from the dictionary

            elif 'ability' in rooms[currentRoom] and move[1] in rooms[currentRoom]['ability']:
                abilities += [move[1]]  # add ability to abilities
                print(crayons.yellow('\nYou have unlocked the ' + move[1].capitalize() + ' ability!\n', bold=True)) # msg saying you received the ability
                #stat_trackerA += 1 # Adds to the stat tracker
                del rooms[currentRoom]['ability']

            else:
                print('Seems that the ' + (move[1].capitalize()) + 'didn\'t appreciate you being so handsy.')

        # Let's you view the decription of your current room.
        if move[0] == 'look':
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc']) # print the look description
            else:
                print('Your vision is a little hazy right now. You should have listened to your squire, ten pints was perhaps a tad too much last night.')

        # Help command for showing instructions
        elif move[0] == 'help':
            showInstructions()

        # Save file, potentially
        #elif move[0] in ['s', 'save]']:
            #save()

        # Quit command, let's you exit the game
        elif move[0] in ['q', 'quit]']:
            print("Are you sure you want to quit? Yes/No")
            quit_query = input('>')
            if quit_query.lower() in ['y', 'yes']:
                print("Thanks for playing!")
                sys.exit()
            else:
                pass

warsong()