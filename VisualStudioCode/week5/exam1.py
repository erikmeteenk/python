def exam1(array1,array2):
    newarray = []
    for i in range (len(array1)):
        x = 0
        x = array1[i] + array2[i]
        newarray.append(x)
    print(newarray)
a = [1,2,3]
b = [4,5,6]
#exam1(a,b)

def exam2():
    n = 5
    for i in range(n):
        for j in range(i):
            print("* ",end=" ")
        print("")
    for k in range(n,0,-1):
        for l in range(k):
            print("* ",end=" ")
        print("")
#exam2()

def exam3():
    array = []
    for i in range(5,8):
        sarray = []
        for j in range(3):
            sarray.append(i)
        array.append(sarray)
    print(array)
#exam3()

def exam4():
    array = [[1,  0,   1,  1,  0 ],
         [0, "x", "x", 0,  0 ],
         [1,  0,   1,  1, "x"],
         [0, "x",  0,  1,  0 ]]
    newarray = []
    for rij in range(1,len(array)):# 4 iteraties met de waarden 1,2,3,4 of 0,1,2,3 indien -1
         for kol in range (0,len(array[rij])-1):# 5 iteraties met de waarden 0,1,2,3 of 1,2,3,4 indien +1
                if (array[rij][kol]) == "x":

                    if (array[rij-1][kol+1]) == 1:
                        sarray = []
                        sarray.append(rij)
                        sarray.append(kol)
                    newarray.append(sarray)
    print(newarray)
exam4()
