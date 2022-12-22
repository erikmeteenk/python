
def matrixuiteenhalen(a):
    nieuwelijst = []
    for i in range(len(a)):
        for j in a[i]:
            nieuwelijst.append(j)
    print("ongesorteerd:",nieuwelijst)
    nieuwelijst.sort()
    print("gesorteerd  :",nieuwelijst)
    nieuwelijst.reverse()
    print("omgekeerd   :",nieuwelijst)
    nieuwelijst.pop(0)
    print("1ste el verw:",nieuwelijst)
    nieuwelijst.remove(7)
    print("7 verwijderd:",nieuwelijst)



a = [[1,32,3],[4,57,6],[7,78,9]]
#matrixuiteenhalen(a)

def matrixoptellen(matrix):
    
    som = 0
    for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            som +=matrix[i][j]
    print(som)

a = [[1,2,3],[4,5,6],[7,8,9]]

#matrixoptellen(a)

def schaduwzoeker(b):
    maninschaduw = []
    for i in range(1,len(b)):
        for j in range((len(b[i])-1)):
            if b[i][j] == "x" and b[i-1][j+1] == 1:
                maninschaduw.append((i,j))
    print(maninschaduw)


a = [[0 ,1, 1,  0, 1],
     [1,"x","x","x",1],
     ["x",1,"x","x",1],
     ["x",0,"x","x",0]]
#schaduwzoeker(a)

def matrixmaken():
    x = int(input("geef het aantal elementen  van de array in:"))
    newarray = []
    for i in range(x):
        y = int(input(f"voer hier getal {i} in:"))
        newarray.append(y)
    print(newarray)

#matrixmaken()
def som():
    x, y = input("geef getallen in: ").split()
    #x = input("geef getallen in: ")
    #y = input("geef getallen in: ")

    z = int(x) + int(y)
    print(z)
#som()
def matrix2Dmaken():
    x = int(input("geef het aantal elementen  van de array in:"))
    newarray = []
    y = int(input("geef het aantal elementen  van de subarray in:"))
    for i in range(x):
        subarray = []
        for j in range(y):
                k = int(input(f"voer hier getal {j+1} van subarray {i+1} in:"))
                subarray.append(k)
        newarray.append(subarray)
    print(newarray)

#matrix2Dmaken()

def splitten():
    x = input("geef getallen in gescheiden door spaties om een array te maken:").split()
    print("Dit is x:",x)
    array = []
    for i in x:
        k = int(i)
        array.append(k)
    print("dit is de resulterende array met integers:",array)
    array.sort()
    print("dit is de gesorteerde array met integers:",array)
    return array
#splitten()
from statistics import mean,median
array = splitten()
print (f"het gemiddelde is:{mean(array):.2f}")
print (f"de mediaan is: {median(array):.2f}")


