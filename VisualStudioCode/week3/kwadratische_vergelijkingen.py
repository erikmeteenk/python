# https://dodona.ugent.be/nl/courses/1721/series/18978/activities/784140866
from math import sqrt
a=int(input("voer hier a in:"))
b=int(input("voer hier b in:"))
c=int(input("voer hier c in:"))
delta=b*b-4*a*c

if a != 0:

    if delta < 0:
        print("Er zijn geen reële oplossingen")
    elif delta == 0:
        x1=(-b-sqrt(delta))/(2*a)
        print("Er is 1 reële oplossing:",x1)
    else:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        print("Er zijn 2 reële oplossingen:",x1,"en",x2)
else:
    print("Ongeldige vergelijking")