def exercise1(array1,array2):
    list=[]
    for i in range(len (array1)):
        x = array1[i] + array2[i]
        list.append(x)
    print(list)


a = [1,2,3]
b = [4,5,6]
#exercise(a,b)
def exercise2():
    n = 5
    for i in range(n):
        for j in range(i):
            print("* ",end="")
        print("")
    for i in range(n,0,-1):
        for j in range(i):
            print("* ",end="")
        print("")

#exercise2()
def exercise3():
    array=[]
    
    for i in range (5,8):
        sarray = []
        for j in range (3):
            x = i
            sarray.append(x)
        array.append(sarray)
    print(array)
#exercise3()
def exercise4(array):
    resultaat = []
    for i in range (1,len(array)):
        for j in range (0,len(array[i])-1):
            if array[i] [j] == "x" and array[i-1] [j+1] == 1:#i is de rij , j is de kolom
                resultaat.append((i,j))
    print(resultaat)

array=  [[1,0,1,1,0],
        [0,"x","x",0,0],
        [1,0,1,1,"x"],
        [0,"x",0,1,0]]
#exercise4(array)

