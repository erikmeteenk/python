#functie1:schrijf een functie die 2 argumenten verwacht
#beide argumenten zijn arrays
#print elk element uit behalve het getal 10

#functie2:schrijf een functie die 1 argument verwacht
#deze functie is een 2d array
#delete alle getallen met waarden 10
a=[1,2,3,4,5,6,7,8,5,10,8,3]
b=[7,8,2,6,4,9,8,10,7,5,8,7]
#print(a),print(b)
def functie1(a,b):
    for i in a:
        if i!=10:
            print(i)
    for j in b:
        if j!=10:
            print(j)
functie1(a,b)