#diego torres
#1/7
#Rock Paper Scissors

#Init
import random

#Function
def RPS():
        #step 1: collect the players move
    print("Welcome to Rock Paper Scissors")
    print("What is your first move?")
    while True:
        player = input("Rock, Paper, Scissors, Go:")
        player = player.lower()

    #step 2: Generate the computer's move
        computer = (random.randint(1, 3))
        if computer == 1:
            computer = "rock"
            print("The cumpter's move is Rock!")
        if computer == 2:
            computer = "paper"
            print("The cumpter's move is Paper!")
        if computer == 3:
            computer = "scissors"
            print("The cumpter's move is Scissors!")

    #step 3: The outcome

        if player == "rock" and computer == "rock":
            print("it is a Tie!")
        elif player == "paper" and computer == "paper":
            print("it is a Tie!")
        elif player == "scissors" and computer == "scissors":
            print("it is a Tie!")
        elif player == "rock" and computer == "scissors":
            print("YOU WONNNNNNNN!!!!")
        elif player == "rock" and computer == "Paper":
            print("You lost")
        elif player == "Paper" and computer == "rock":
            print("YOU WONNNNNNNN!!!!")
        elif player == "Paper" and computer == "scissors":
            print("You lost")
        elif player == "scissors" and computer == "paper":
            print("YOU WONNNNNNNN!!!!")
        elif player == "scissors" and computer == "rock":
            print("You lost")

    #step 4: loop the game until the player wants to quit
        playagain = input("Do you want to keep playing")
        if playagain == "yes":
            print("restarting....")
        else:
            print("Thank you for playing")
            break
#Main
RPS()




