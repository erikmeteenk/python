from sys import exit

teller = 0
laagste = 0
hoogste = 101
print( "neem een getal in gedachten tussen 1 en 100." )

while True:
    gissing = int( (laagste + hoogste) / 2 )
    print(f"mijn gok is:{gissing}")
    teller += 1
    antwoord = input( "voer H, L of C in:" )
    if antwoord == "C":
        break
    elif antwoord == "L":
        hoogste = gissing
    elif antwoord =="H":
        laagste = gissing
    else:
        print( "voer H, L of C in:" )
        continue
    if laagste >= hoogste-1:
        print( "Je moet je vergissen,", 
            "want je zegt hoger dan",
            laagste, "maar lager dan", hoogste )
        print( "Ik stop ermee" )
        exit()

if teller == 1:
    print( "Ik had slechts 1 gissing nodig! Ik ben een genie." )
else:
    print( "Ik had", teller, "gissingen nodig." )