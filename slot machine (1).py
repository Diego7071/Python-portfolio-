#Diego Torres
#slot Machine
#init
import random
symbols = ["7", "♠"  , "♡" , "♢" , "♣" , "✿" , "✪"]
credits = 100
#Function


#Main


#1. Introduction
#2. Ask the player, spin or quit
#3. randomly pull 3 intesm from the list
#Advice: make sure you store these in a variable
#4.desplay the 3 images
#5.deteremine the outcome(IF ELIS ELSE)

#Credit system
#add more symbols
#1.Evry
#2.Every spin costs 1(chocice)


print("Welcome to THE SLOT MACHINE")
print("To play you need to spin the slot machine\n")
print("you have 100 credits, each spin cost 10 credicts\n")
while True:
    spin = input("Would you like to spin the machine? or quit (S/Q)")
    if spin == "S":
        bet = int(input("how much credits would you like to bet?(The more you bet the higher you win)"))
        credits = credits - bet
        print("If you out of credits you will not be able to spin again")
        slot1 = random.choice(symbols)
        slot2 = random.choice(symbols)
        slot3 = random.choice(symbols)
        random.choices(symbols, weights = [1,5,8,5,5,5,5])


        print(  "\n" + "                  " + slot1 + slot2 + slot3 +"\n")
        if slot1 == "7" and slot2 == "7" and slot3 == "7":
            print("congratulations!!!! YOU WON THE JACKPOT!!!!\n")
            credits = credits + 100 * bet
            print("you have " + str(credits))
        elif slot1 == slot2 and slot1 == slot3:
            print("congratulations!!!! YOU Got three in a row!!!!\n")
            credits = credits + 20 * bet
            print("you have " + str(credits))
        elif slot2 == slot1 or slot2 == slot3:
            print("congratulations!!!! YOU Got two in a row!!!!\n")
            credits = credits + 5 * bet
            print("you have " + str(credits))
        elif slot1 == slot2 or slot1 == slot3:
            credits = credits + 5 * bet
            print("congratulations!!!! YOU Got two in a row!!!!\n")
            print("you have " + str(credits))
        elif slot3 == slot2 or slot3 == slot1:
            print("congratulations!!!! YOU Got two in a row!!!!\n")
            credits = credits + 5 * bet
            print("you have " + str(credits))
        else:
            print("you lost :(\n")
            print("you have " + str(credits))
    if spin == "Q":
        print("Understand, Have a nice day.")
        break


