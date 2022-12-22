# efficient version

def goDirection(d):
    print("you go " + d)

first_d = input("Give the first direction (left, right, up or down): ")
direction_list = ["left", "right", "down", "up"]

if first_d in direction_list:
    goDirection(first_d)
else:
    print("the direction is not correct")


#Not efficient
def goDown():
    print("your are going down")

def goUp():
    print("your are going up")

def goLeft():
    print("your are going Left")

def goRight():
    print("your are going right")

def direction():
    d = input("Which direction you wanne go?(R,L,U,D)")
    if d == "R":
        goRight()
    elif d == "D":
        goDown()
    elif d == "U":
        goUp()
    elif d == "L":
        goL()

direction()