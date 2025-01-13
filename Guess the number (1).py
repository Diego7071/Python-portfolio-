#diego Torres
#11/8

#init
import random

#function
def Guess_the_number():
    num = int(random.randint(1, 10))
    ans = input("Would you like to play a game?(Yes,No)")
    if ans == ("No"):
        print("ok")
        print(":(")
        print("Have a Good Day")
    if ans == ("Yes"):
        for i in range(3):
            guess = int(input("Guess a Number Between 1-10"))
            if guess == num:
                print("congratulating!!!!!!")
                print("Your Guess Is Correct")
                break
            elif guess < num:
                print("TOO LOWWWW")
            elif guess > num:
                print("TOO HIGHHHHH")
                print(" ")
        if guess != num:
                print(" ")
                print("Your Guess was Wrong")
                print(":(")
                print("the correct number was " + str(num))
        print(" ")
        print("Thank You For Playing")








#main

Guess_the_number()

