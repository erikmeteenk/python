def elsebijloop():
    i = 0
    while i < 5:
        print(i)
        i +=1
    else:
        print("de loop eindigt, i is nu ",i)
    print("klaar")
#elsebijloop()
def elsebijforloop():
    for fruit in ("appel","peer","banaan"):
        print(fruit)
    else:
        print("de loop eindigt, fruit is nu ",fruit)
    print("klaar")
#elsebijforloop()
def loopmetbreak():
    i = 1
    while i<1000000:
        num1 = int("1" + str(i))
        num2 = int(str(i) + "1")
        #print(num1)
        #print(num2)
        if num2 == 3 * num1:
            print(num2,"is drie keer",num1)
            break
        i += 1
    else:
        print("geen antwoord gevonden")
#loopmetbreak()
def forloopmetbreak():
    z=[8,9,5.5,6,6.5,8.5,5,10]
    for cijfer in (z):
       if cijfer < 5.5:
        print("gezakt")
        break 
    else:
        print("geslaagd")
#forloopmetbreak()
def loopmetcontinue():
    num = 0
    while num < 100:
        num +=1
        if num%2 == 0:
            continue
        if num%3 == 0:
            continue
        if num%10 == 7:
            continue
        if num%10 == 9:
            continue
        print(num)
#loopmetcontinue()
def loopmetforcontinue():
    lijst = [12,4,3,33,-2,-5,7,22,4]
    totaal = 0
    for i in lijst:
        if i == 0:
            break
        if i < 0:
            continue
        else:
            totaal +=i
            
    print("totaal is:",totaal)
    print("klaar")

#loopmetforcontinue()
def genesteloop():

    for i in range(1,4):
        #print("dit is de eerste waarde van i in de buitenste loop",i)
        for j in range (1,4):
            #print("dit is de eerste waarde van J:",j)
            if i == j:#dit verhindert het afdrukken van gelijke paren
                continue
            print(f"       (i,j) = ({i},{j})")
            #print("dit is de laatste waarde van J:",j)
    #print("dit is de laatste waarde van i in de buitenste loop",i)    

#genesteloop()
def loopeneenhalf():
    while True:
        x=int(input("voer getal 1 in :"))
        if x == 0:
            print("hier stopt het!")
            break
        y=int(input("voer getal 2 in :"))
        if y == 0:
            print("hier stopt het!")
            break
        """"if x == 0 or y == 0:
            print("hier stopt het!")
            break"""
        if x > 1000 or y > 1000:
            print("bereik is 1 tot duizend dus nieuwe getallen ingeven!")
            continue
        if (x % y) == 0 or (y % x) == 0:
            print("getallen mogen geen delers zijn, dus nieuwe getallen ingeven!")
            continue
        
        print(f"het product van {x} en {y} is:",x*y)
    print("klaar")
#loopeneenhalf()
def loopeneenhalf2():
    while True:
        x=int(input("voer een positief getal in :"))
        if x >= 0:
            break

        if x < 0:
            print("geen positief getal dus opnieuw!")
            continue
        
        
    print(x)
    print("klaar")
#loopeneenhalf2()
def dobbelstenen6():
    from random import randint
    aantalTests =  1000000
    succes = 0
    for i in range (aantalTests):
        for j in range(5):
            if randint(1,6) != 6:
                break
            else:
                succes += 1
    print ("de waarschijnlijkheid is:", succes/aantalTests )
    print(1/(6**5))
#dobbelstenen6()
def minimax():
    lijst = [1,4,56,89,45,78,23,180,250]
    x = min(lijst)
    y = max(lijst)
    print ("kleinste:",x,"grootste:",y)

#minimax()
def grootklein3():
    lijst = [1,4,56,89,45,78,23,180,250]
    teller3 = 0
    kleinste = 0
    grootste = 0
    for i in range (10):
        getal=int(input(f"geef getal {i+1} in:"))
        if getal % 3 ==0:
            teller3 +=1
        if i == 0:
            kleinste = getal
            grootste = getal
            continue
        if grootste < getal:
            grootste = getal
        if kleinste > getal:
            kleinste = getal
    print("grootste:", grootste, "kleinste:", kleinste, "en deelbaar door 3:", teller3)
grootklein3()











