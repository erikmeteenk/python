aantal_piraten = int(input("geef het aantal piraten in: "))
cocosnoten = 0
while True:
    cocosnoten += 1
    stapel = cocosnoten
    for i in range( aantal_piraten ):
        if stapel % aantal_piraten != 1:
            break
        stapel = (aantal_piraten-1) * int( (stapel - 1) / aantal_piraten )
    if stapel % aantal_piraten == 1:
        break
print( cocosnoten )