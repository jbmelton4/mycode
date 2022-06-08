#!/usr/bin/env python3

##GOALS
# Make a "Which DBZ character are you?" Quiz.
# Return unique answers based on the input provided... multiple results should be possible.
#AS BEST YOU'RE ABLE, control for user errors (suggested: methods, try/except, while loop)
#Use at least one while loop.
#Make all code "your own."
#ROUGH minimum of 40 lines of code... if code is spread out across multiple files, they are cumulative.

#character total

user_total = 0

print("Which DBZ Character are you? I have no idea, answer these totally unbiased questions to figure it out:")
print()
print()

while True:
    
    q1_answer = input("Which fruit do you prefer? \na) Tomato, \nb) Apple, \nc) Pineapple, \nd) Grapes, \ne) I don't like fruit because I'm weird like that.")
    if q1_answer.lower() == 'a':
        user_total += 2
        break
    elif q1_answer.lower() == 'b':
        user_total += 10 
        break
    elif q1_answer.lower() == 'c':
        user_total += 8 
        break
    elif q1_answer.lower() == 'd':
        user_total += 4 
        break
    elif q1_answer.lower() == 'e':
        user_total += 6 
        break
    else:
        print()
        print("The dragonballs couldn't help you with that answer, try again.")
        print()
        continue

while True:

    q2_answer = input("What kind of job would you like? \nA) President \nB) Working is for squares \nC) Teacher \nD) Park ranger \nE) I rely on my sugar mama/daddy")
    if q2_answer.lower() == 'a':
        user_total += 8 
        break
    elif q2_answer.lower() == 'b':
        user_total += 10 
        break
    elif q2_answer.lower() == 'c':
        user_total += 4 
        break
    elif q2_answer.lower() == 'd':
        user_total += 6 
        break
    elif q2_answer.lower() == 'e':
        user_total += 2 
        break
    else: 
        print()
        print("Bubbles is making obscene gestures, I don't think that works. Try again.")
        print()
        continue 
 
while True:

    q3_answer = input("What color do you like? \nA) Purple \nB) Blue \nC) Yellow \nD) Green \nE) Red")
    if q3_answer.lower() == 'a':
        user_total += 6
        break
    elif q3_answer.lower() == 'b':
        user_total += 10
        break
    elif q3_answer.lower() == 'c':
        user_total += 2
        break
    elif q3_answer.lower() == 'd':
        user_total += 4
        break
    elif q3_answer.lower() == 'e':
        user_total += 8
        break
    else:
        print()
        print("Oh no! You summoned a dragon on steroids! Check out his delts! Dude, he looks like he lifts, let's get out of here and try again.")
        print()
        continue

while True:

    q4_answer = input("What kind of shoes do you wear? \nA) Slippers \nB) Converse \nC) Hiking boots \nD) Nikes \nE) Crocs")
    if q4_answer.lower() == 'a':
        user_total += 6
        break
    elif q4_answer.lower() == 'b':
        user_total += 4
        break
    elif q4_answer.lower() == 'c':
        user_total += 10
        break
    elif q4_answer.lower() == 'd':
        user_total += 8
        break
    elif q4_answer.lower() == 'e':
        user_total += 2
        break
    else:
        print()
        print("You should try fusing with Kami, that might put you on the right track. Try again.")
        print()
        continue


while True:

    q5_answer = input("Someone smacks you in the face, how do you respond? \nA) Challenge them to a duel! They dare touch me?!  \nB) Hit them back!  \nC) Retaliation isn't the answer. \nD) Steal their dog. \nE) Pathetic, I laugh it off.")
    if q5_answer.lower() == 'a':
        user_total += 8
        break
    elif q5_answer.lower() == 'b':
        user_total += 10
        break
    elif q5_answer.lower() == 'c':
        user_total += 4
        break
    elif q5_answer.lower() == 'd':
        user_total += 2
        break
    elif q5_answer.lower() == 'e':
        user_total += 6
        break
    else:
        print()
        print("It's not over 9000. Try again.")
        print()
        continue

if user_total in range(10,18):
   print ("Congrats! You are...Yamcha. Huh. Bro, why are you even here? You were pretty cool back in the day but you got quickly overshadowed by your friends. Even that weird bald kid ended up surpassing you. I'd say you did pretty well on the love front but a spikey-headed alien stole your girl. You're pretty good at sports, you have a weird relationship with your cat, but at least you're better than the average joe.")

elif user_total in range(19,28):
    print ("Congrats! You are Gohan.")
