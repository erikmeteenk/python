# https://dodona.ugent.be/nl/courses/1721/series/18979/activities/798810280
from sys import exit

teller = 0
laagste = 0
hoogste = 101
print( "neem een getal in gedachten tussen 1 en 100." )
while True:
    gissing = int((laagste + hoogste)/2)
    teller +=1
    print("mijn gissing is:",gissing)
    antwoord = input("voer in H,L of C: ")
    if antwoord == "C":
        break
    if antwoord == "H":
        laagste = gissing
    if antwoord == "L":
        hoogste = gissing
if teller == 1:
    print("Direct juist dus")
else:
    print("Dit is dus de juiste oplossing:",gissing,"gevonden in",teller,"beurten")

