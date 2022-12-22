def quest1():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sum = 0
    for i in matrix:
        for j in i:
            sum +=j
    print(sum)
#quest1()

def quest2():
    myList = [3,12,"pizza",3,4]
    print(len(myList))
    for i in range(len(myList)):
        print(f"element met index {i} : {myList[i]}")
#quest2()

def quest3():
    array = [12,43,"Y",44,"X"]
    newarray = []
    for i in array:
        subarray = []
        if  type(i) == int:
            for j in range(3):
                subarray.append(i)
        if type(i) == str:
            for k in range(2):
                subarray.append(i)
        newarray.append(subarray)
    print(newarray)
#quest3()
def quest4():
    array = [[1,3,1,1,4],[2,4,3,1,2],[3,5,4,1,1],[4,6,2,1,4]]
    newarray = []
    for i in range(len(array[0])):
        sum = 0
        for j in range(len(array)):
            sum += array[j][i]
        newarray.append(sum)
    print(newarray)
quest4()
    





