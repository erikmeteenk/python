# https://dodona.ugent.be/nl/courses/1721/series/18979/activities/1150748783
from random import random
from math import sqrt
n=int(input("voer het aantal worpen in:"))
m=0
for i in range(n):
    x=random()
    y=random()
    z=sqrt(x*x+y*y)
    if z < 1:
        m +=1

print((4*m)/n)

