#functie1:schrijf een functie die 2 argumenten verwacht
#beide argumenten zijn arrays
#print elk element uit behalve het getal 10

#functie2:schrijf een functie die 1 argument verwacht
#deze functie is een 2d array
#delete alle getallen met waarden 10

#print(a),print(b)
array=[[1,2,3,4,5,10,8,3],[8,10,7,5,8,7],[7,8,2,6,4,9,8,10]]
def functie2(a):
    newArray = []
    for i in array:
        subArray = []
        for k in i:
            if k!=10:
                subArray.append(k)
                print(k)
        newArray.append(subArray)
        print(newArray)
    return newArray

functie2(array)

