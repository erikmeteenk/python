import operator

def exercise1(array1,array2):
    c = list(map(operator.add, array1,array2))
    print(c)

a = [1, 2, 3]
b = [4, 5, 6]
#exercise1(a,b)


def exercise2():
    n=5;
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')

def exercise3():
    array = []
    for i in range(5,8):
        sArray = []
        for k in range(3):
            sArray.append(i)
            
        array.append(sArray)

    print(array)

def exercise4(array):
    newArray = []
    for i in range(1, len(array)):
        for k in range(len(array[i])-1):
            if array[i][k] == "x":
                if array[i-1][k+1] == 1:
                    newArray.append((i,k))
    
    print(newArray)

array = [[1,  0,   1,  1,  0 ],
         [0, "x", "x", 0,  0 ],
         [1,  0,   1,  1, "x"],
         [0, "x",  0,  1,  0 ]]
exercise4(array)      
