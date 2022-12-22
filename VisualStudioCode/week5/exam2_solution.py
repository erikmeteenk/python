
def exercise1(matrix):
    sum = 0
    for i in matrix:
        for k in i:
            sum += k
    print(sum)

matrix = [[11,12,13],
          [14,15,16],
          [17,18,19]]

exercise1(matrix)

def exercise2(myList):
    myList = [3, 12, "pizza", 3, 4]
    print("myList heeft lengte", len(myList))
    for i in range(0, len(myList)):
        print("element met index", i, ":", myList[i])

myList = [3, 12, "pizza", 3, 4]
exercise2(myList)

def exercise3(array):
    newArray = []
    for i in array:
        sArray = []
        if(isinstance(i, int)):
            for k in range(3):
                sArray.append(i)
        if(isinstance(i, str)):
            for k in range(2):
                sArray.append(i)
        newArray.append(sArray)
    print(newArray)

a = [12, 43, "Y", 44, "X"]
exercise3(a)

def exercise4(array):
    newArray = []
    for i in range(len(array[0])): #kolom
        sum = 0
        for k in array:    #rij
            sum += k[i]
        newArray.append(sum)
    print(newArray)


array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]
        
exercise4(array)