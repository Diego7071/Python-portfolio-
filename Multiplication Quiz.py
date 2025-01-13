#Diego Torres
#1/9
#Multiplication Quiz

#init
import random
import time
correct = 0
question = 1
#Function

def multiplication_quiz():
    global correct
    global question
    print("""Welcome to The Multiplication Quiz


      """)
    Q = input("how much questions would you like to do?")
    Q = int(Q)
    level = input("pick a level: easy, medium, or hard")
    if level == "easy":
        start_time = time.time()
        for i in range(Q):
            print("Question " + str(question) + " out of " + str(Q))
            num1 = random.randint(1,5)
            num2 = random.randint(1,10)
            print("what is " + str(num1) + "x" + str(num2))
            answer = input("what is " + str(num1) + "x" + str(num2))
            print("Your answer: " + answer)
            cal = num1 * num2
            if answer == str(cal):
                print("Correct!")
                correct = correct + 1
            else:
                print("Wrong")
            question = question + 1
            print("")
    elif level == "medium":
        start_time = time.time()
        for i in range(Q):
            print("Question " + str(question) + " out of " + str(Q))
            num1 = random.randint(1, 10)
            num2 = random.randint(1,15)
            print("what is " + str(num1) + "x" + str(num2))
            answer = input("what is " + str(num1) + "x" + str(num2))
            print("Your answer: " + answer)
            cal = num1 * num2
            if answer == str(cal):
                print("Correct!")
                correct = correct + 1
            else:
                print("Wrong")
            question = question + 1
            print("")
    elif level == "hard":
        start_time = time.time()
        for i in range(Q):
            print("Question " + str(question) + " out of " + str(Q))
            num1 = random.randint(1,20)
            num2 = random.randint(10,20)
            print("what is " + str(num1) + "x" + str(num2))
            answer = input("what is " + str(num1) + "x" + str(num2))
            print("Your answer: " + answer)
            cal = num1 * num2
            if answer == str(cal):
                print("Correct!")
                correct = correct + 1
            else:
                print("Wrong")
            question = question + 1
            print("")

    end_time = time.time()
    elapsed_time = end_time - start_time


    print("you got " + str(correct) + " out of the " + str(Q) + " quesions!")
    print("you have competec the quiz in " + str(elapsed_time) + " seconds")


#Main
multiplication_quiz()
