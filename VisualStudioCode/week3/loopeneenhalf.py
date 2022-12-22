
from sys import exit

while True:
    x = int(input( "Geef nummer in: " ))
    if x == 0:
        break
    if (x < 0 ):
        print( "Nummers moeten positief zijn" )
        continue
    print(x)
    

