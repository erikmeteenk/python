from random import random, randint
x = randint(1,100)#stel 51 en getal is 75
print(f"dit is het getal waaraan de computer denkt:{x}")
y = input("voer H,L of C in:")
def moduleH(x,y):
    for i in range(1,100):
        if y == "C":
            print("correct")
            break
            for j in range(50):
                y=input("H,L of C invoeren:")
                if y == "H":
                    x = randint(x,100)
                    print(x)
            if y =="L":
                moduleH(x,y)
            else:
                if y == C:
                    print("correct")
                    break
def moduleL(x,y):
    for k in range(1,100):
        if y == "C":
            print("correct")
            break
    for l in range(50):
        y=input("H,L of C invoeren:")
        if y == "L":
            x = randint(x,100)
            print(x)
        if y =="H":
             moduleH(x,y)
        else:
            if y == C:
                print("correct")
                break
            
moduleH(x,y)