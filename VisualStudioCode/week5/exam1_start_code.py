
from re import I


def exercise1(a,b):
    newarray = []
    for i in range (len(a)):
        x = a[i] + b[i]
        newarray.append(x)
    print(newarray)
    
a = [1,2,3]
b = [4,5,6]
#exercise1(a,b)

def exercise2():
    n = 5
    for i in range(n):
        for j in range(i):
            print("* ",end="")
        print("")
    for i in range(n,1,-1):
        for j in range(i):
            print("* ",end="")
        print("")
#exercise2()


def exercise3():
    newarray = []
    for i in range (5,8):
        sarray = []
        for j in range (3):
            sarray.append(i)
        newarray.append(sarray)
    print(newarray)
#exercise3()


def exercise4(array):
    newarray = []
    for i in range(1,len(array)):
        for j in range(len(array)):
            if array[i][j] == "x":
                if array[i-1][j+1] == 1:
                    newarray.append((i,j))
    print(newarray)
array = [[1,  0,   1,  1,  0 ],
         [0, "x", "x", 0,  0 ],
         [1,  0,   1,  1, "x"],
         [0, "x",  0,  1,  0 ]]
        
exercise4(array)