from random import random, randint
from sys import exit
x = randint(1,1000)
teller = 1
print (x)
while True:
    invoer = int(input("voer je gis in:"))
    if invoer == x:
        print("juist")
        break
    teller +=1
    if invoer < x:
        print ("hoger")
    else:
        print("lager")
    if invoer == 0:
        exit()
print("klaar")
print("aantal gissingenn:",teller) 