def van1tot5():#701
    num = 1
    while num <= 5:
        print(num)
        num +=1
    print("klaar")
#van1tot5()
def invoer5():#702
    totaal = 0
    teller = 0
    while teller < 5:
        teller += 1
        totaal += int(input(f"voer getal {teller} in:"))
    print("totaal is :", totaal)
    print("gemiddelde is :",int(totaal/teller))
#invoer5()
def invoeronbeperkt():
    totaal = 0
    num = -1
    while num !=0:
        num = int(input("voer getal in:"))
        totaal += num
    print("totaal is :", totaal)
#invoeronbeperkt()
def invoeronbeperkt2():
    totaal = 0
    num = int(input("voer getal in:"))
    while num !=0:
        totaal += num
        num = int(input("voer getal in:"))
        
    print("totaal is :", totaal)
#invoeronbeperkt2()
def gevaareindeloos():
    nummer = 1
    totaal = 0
    while (nummer*nummer) % 1000 != 0:
        totaal += nummer
        nummer += 1
    print("Totaal is:",totaal)
#gevaareindeloos()
def aftellen():
    nummer = 10
    while nummer > 0:
        print(nummer)
        nummer -= 1
    print("start")
#aftellen()
def faculteit():
    invoer = int(input("voer het getal in waarvan je de faculteit wil berekenen:"))
    teller = 0
    x = invoer
    fac = 1
    while teller < x:
        fac *= invoer
        invoer -= 1
        teller += 1
    print(f"{x}! = ",fac)
#faculteit()
def banaan():
    for letter in "banaan":
        print (letter)
    print("klaar")
#banaan()
def fruit():
    fruit = "banaan"
    for letter in fruit:
        print (letter)
        if letter == "n":#deze en volgende regel illusteren dat de reeks binnen de loop niet meer kan wijzigen
            fruit = "mango"
    print("klaar")
#fruit()
def veelvoudenvan3():
    for x in range(21,1,-3):
        print(x)
#veelvoudenvan3()
def metcollectie():
    collectie = [0,1,1,2,3,5,8,13,21,34]
    collectie2 = ["appel","peer","appelsien","mango","banaan"]
    for i in (collectie):
        print(i)
        for j in (collectie2):
            print(j)
    print("klaar")
#metcollectie()
def forloop5():
    totaal = 0
    for i in range(5):
        x = int(input("voer getal in:"))
        totaal +=x
    print(totaal)
#forloop5()
def foraftellen():
    for i in range(10,1,-1):
        print(i)
    print("start")
#foraftellen()


