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

if user_total in range(10,19):
   print ("Congrats! You are...Yamcha. Huh. Bro, why are you even here? You were pretty cool back in the day but you got quickly overshadowed by your friends. Even that weird bald kid ended up surpassing you. I'd say you did pretty well on the love front but a spikey-headed alien stole your girl. You're pretty good at sports, you have a weird relationship with your cat, but at least you're better than the average joe.")

elif user_total in range(19,28):
    print ("You are Gohan. That's cool, nerd. You're intelligent, diligent, and a bit of a dweeb but that's okay. You have everyone's best interests at heart! You were one of the most powerful beings in the known universe. Most people peak in their 30s or 40s but you peaked at 10...it was pretty much all downhill from there on the whole 'strongest on the earth' front. It's okay though, just go home and be a family man.")

elif user_total in range(28,38):
    print ("Congrats! You are Piccolo! I am green with envy. Har har. Seriously though, it's not easy being green. You're stoic, calm, and a natural born teacher. Your dad was kind of a prick and you started off down the same path before you found your way. It only took the friendship of a small boy and absorbing several of your species into your conciousness to put you on the path of good! Um...well, anyways, good job!")

elif user_total in range(38,44):
    print ("All hail the might Prince of all Saiyans, Vegeta! You are a person of sm...mighty stature! Sure, you have a serious anger problem but you're dedicated as hell. Seriously, you had more character development than the main protagonist. Don't feel bad you'll never surpass them, Akira Toriyama hates you and only uses you begrudgingly to make the main character look good. Hey, you love your family and have found a home where you least expected it. Plus your spouse is loaded, so at least you don't have to worry about paying for anything ever.")

elif user_total in range(44,51):
    print ("Yay, you're the main character, Goku! You are the mold that all other protagonist will be based off forall time. I don't know how to tell you this, but that's pretty basic. You're not the smartest and you were pretty ripped in the 90s before you got into crossfit or something.  Look, we get it, you're strong and like to fight. So much that you've let your son be raised by an alien who swore to kill you just so you didn't have to and you ignore your wife unless she has food for you. To be fair you thought Piccolo was a demon, not an alien...wait, that's worse. Death can't keep you down from deckin' a baddie in the shnoz though, you always show up at the last minute to save the day, and you dyed your hair blonde before everyone else so that's cool I guess. This totally isn't a biased opinion. You do you, Son.")
