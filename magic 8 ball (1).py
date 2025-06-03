#Diego Torres


#init
import random
mylist = ["It is certain" ,	"Reply hazy", "try again", "Don’t count on it" , "It is decidedly so" , "Ask again later" ,"My reply is no", "Without a doubt","Better not tell you now","My sources say no","Yes definitely", "Cannot predict now"	, "Outlook not so good","You may rely on it","Concentrate and ask again","Very doubtful","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes"]

#Function
def Magic8ball():
    #introdusction
    #ask thge player to enter a question
    #Randomly slect from your list and dislapy a respon
    #loop
    global mylist
    print("I am the magic 8 ball")
    print("Ask me a question and I give you an answer\n")
    while True:
        question =input("what is your question?\n")
        print(question + "\n")
        x = question.endswith("?")
        if x == True:
            print("my answer is")
            print(random.choice(mylist) + "\n")

        if x == False:

            print("ERROR:Not a question(try adding an ?)\n")
        again = input("would you like to ask more questions?(Y/N)\n")
        if again == "Y":
            print("Have fun asking questions\n")
        if again == "N":
            print("ok, have a great day")
            break


#main

Magic8ball()

