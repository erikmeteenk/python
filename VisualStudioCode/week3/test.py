from calendar import c
from random import random, randint
x = randint(1,100)#stel 51 en getal is 75
print(f"dit is het getal waaraan de computer denkt:{x}")
y = input("voer H,L of C in:")
for i in range (100):
    if y == "H":
        x = randint(x,100)#dus nieuw poging hoger
        print(x)
    y = input("voer H,L of C in:")
    if y == "L":
        x = randint(1,x)#dus nieuw poging lager
        print(x)
    y = input("voer H,L of C in:")
 
"""for i in range(100):
    print(x)
    y = input("voer H,L of C in:")
    if y == "C":
        print("gevonden!")
        break
    if y == "H":
        for j in range (x):
            print(x)
            y = input("voer H,L of C in:")
            x = randint(x,100)
          
    if y == "L":
        print(x)
        y = input("voer H,L of C in:")
        x = randint(1,x)
        continue"""
   

