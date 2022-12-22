
def exercise1(array2D):
    som = 0
    for i in array2D:
        for j in i:
            som += j
    print(som)

    
a = [[1,2,3],[4,5]]
#exercise1(a)

def exercise2():
    newarray = []
    for i in range(1,21):
        x = i**2
        newarray.append(x)
    print(newarray)


#exercise2()
def exercise3(x, y, z):
    l = 0
    if x == y or y == z or x == z:
        l = 0
    else:
       l = x + y + z
    return l

a = 6
b = 3
c = 2
#print(exercise3(a,b,c))
    

def exercise4(array1, array2):
    newarray = []
    for i in range(len(array1)):
        x = array1[i] + array2[i]
        newarray.append(x)
    return newarray


    
a = [1,2,3,4]
b = [5,6,7,8]
#print(exercise4(a,b))


def exercise5(array):
    newarray = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] % 3 == 0:
                newarray.append((i,j))
    return newarray
    #print(newarray)

array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]
#print(exercise5(array))

