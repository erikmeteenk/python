
def exercise1(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            sum +=j
    print(sum)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#exercise1(matrix)

def exercise2(myList):
    x = len(myList)
    print(f"mylist heeft lengte {x}")
    for i in range(len(myList)):
        print(f"element met index {i} : {myList[i]}")

myList = [3, 12, "pizza", 3, 4]
#exercise2(myList)

def exercise3(array):
    newarray = []
    for i in array:
        sarray = []
        if isinstance(i,int):
            for j in range(3):
                sarray.append(i)
        if isinstance(i,str):
            for k in range(2):
                sarray.append(i)
        newarray.append(sarray)
    print(newarray)
   
    
a = [12, 43, "Y", 44, "X"]
#exercise3(a)

def exercise4(array):
    newarray = []
    for i in range(len(array[0])):
        x = 0
        for j in range(len (array)):
            x += array[j][i]
        newarray.append(x)
    print(newarray)
        


array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]
        
exercise4(array)