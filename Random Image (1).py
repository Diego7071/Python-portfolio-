#Random Image recommender
#Diego Torres


#init
movies = ["https://tinyurl.com/mwr44kh8", #Arrival
"https://tinyurl.com/2b95xjr9", #Scott pilgrim vs. the world
"https://tinyurl.com/3fnvuutj", #waves
"https://tinyurl.com/2d5mhess", #Ready player one
"https://tinyurl.com/4sykrnrk", #Interstellar
]

from PIL import Image
import requests
from io import BytesIO

import random

#Function

def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def movie():
    global movies
    while True:
        ans = input("would you like to get a recommendation?(Y,N)")
        if ans == "Y":
            num = random.randint(0,4)
            if num == 0:
                open_image(movies[0])
                print("your recommendation is Arrival")
                print("movies description")
                print("----------------------------------")
                print("""Linguist Louise Banks leads a team of investigators when gigantic
    spaceships touch down around the world. As nations teeter on the verge of global war, Banks
    and her crew must find a way to communicate with the extraterrestrial visitors.""")
            if num == 1:
                open_image(movies[1])
                print("your recommendation is Scott Pilgrim VS. The World")
                print("movies description")
                print("----------------------------------")
                print(""""In a magically realistic version of Toronto, a young man must defeat
    his new girlfriend's seven evil exes one by one in order to win her heart.""")
            if num == 2:
                open_image(movies[2])
                print("your recommendation is Waves")
                print("movies description")
                print("----------------------------------")
                print("""Traces the journey of a suburban family - led by a well-intentioned but
    domineering father - as they navigate love, forgiveness, and coming together in the
    aftermath of a loss.""")
            if num == 3:
                open_image(movies[3])
                print("your recommendation is Ready Player One")
                print("movies description")
                print("----------------------------------")
                print("""When the creator of a virtual reality called the OASIS dies, he makes a
    posthumous challenge to all OASIS users to find his Easter Egg, which will give the
    finder his fortune and control of his world.""")
            if num == 4:
                open_image(movies[4])
                print("your recommendation is Interstellar")
                print("movies description")
                print("----------------------------------")
                print("""When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot,
    Joseph Cooper,is tasked to pilot a spacecraft, along with a team of researchers, to find a
    new planet for humans.""")

        if ans == "N":
            print(" ")
            print("Have a great day")
            break


    # open_image(movies[0])
    # open_image(movies[1])
    # open_image(movies[2])
    # open_image(movies[3])
    # open_image(movies[4])


    #Arrival image from https://www.imdb.com/title/tt2543164/ (Arrival (2016) Forest Whitaker, Amy Adams, and Jeremy Renner in Arrival (2016))
    #Scott pilgrim vs. the world image from https://www.imdb.com/title/tt0446029/ (Scott Pilgrim vs. the World (2010) Michael Cera in Scott Pilgrim vs. the World (2010)
    #waves image from https://www.imdb.com/title/tt8652728/ (Waves (2019) Sterling K. Brown and Taylor Russell in Waves (2019))
    #Ready player one image from https://www.imdb.com/title/tt1677720/ (Ready Player One (2018) Steven Spielberg, Ben Mendelsohn, George Michael, Simon Pegg, Mark Rylance, Perdita Weeks, Kamara Benjamin Barnett, Mandy June Turpin, T.J. Miller, Lena Waithe, Stephen Mitchell, Neet Mohan, Win Morisaki, Elliot Barnes-Worrell, Kae Alexander, Sarah Sharman, Robert Gilbert, Raed Abbas, Letitia Wright, Tye Sheridan, Asan N'Jie, Hannah John-Kamen, Cara Theobold, Olivia Cooke, Alphonso Austin, Amy Clare Beales, Jane Leaney, Kathryn Wilder, and Philip Zhao in Ready Player One (2018))
    #Interstellar image from https://www.imdb.com/title/tt0816692/ (Interstellar (2014) Matthew McConaughey in Interstellar (2014))


#Main


movie()
