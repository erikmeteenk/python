from random import randint
x = randint(1,100)
print (x)
counter = 1
y = input("voer H,L of C in:")
print(y)
for i in range(1,5):
    if y == "H":
        print("hoger")
        x = randint(x,100)
        print(x)
        y = input("voer H,L of C in:")
    if y == "L":
        print("lager")
        
    if y == "C":
        print("goed gegokt")
