#Diego Torres
#10/23

#init

#Functions
def bottles():
    milk = 99
    for i in range(99):
        if milk > 1:
            print(str(milk) + " bottles of milk on the wall")
            print(str(milk) + " bottles of milk")
            print("Take one down, pass it around")
            milk = milk - 1
            print(str(milk) + " bottles of milk on the wall")
            print()
        else:
            print(str(milk) + " bottle of milk on the wall")
            print(str(milk) + " bottle of milk")
            print("Take one down, pass it around")
            milk = milk - 1
            print(str(milk) + " bottles of milk on the wall")
            print()




#main
bottles()
