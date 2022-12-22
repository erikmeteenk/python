def exam1():#aantal getallen deelbaar door 3
    array = [4,5,6,7,100,200,99]
    teller = 0
    for i in array:
        if i % 3 == 0:
            teller +=1
    print(teller)
#exam1()
def exam2():#oneven posities uitprinten
    array = [4,5,6,7,100,200,99]
    for i in range(len(array)):
        if array[i] % 2 != 0:
            print(i)
#exam2()
def exam3():#alle getallen uit de subarrays optellen
    sum = 0
    array = [[2,4],[5,6],[3,2]]
    for i in array:
        for j in i:
            sum +=j
    print(sum)
#exam3()
def exam4():#alle getallen uit de subarrays in nieuwe array zetten 
    array = [[2,4],[5,6],[3,2]]
    newarray = []
    for i in array:
        for j in i:
            newarray.append(j)
    print(newarray)
#exam4()
def exam5():
    newarray = []
    for i in range(1,4):
        subarray = []
        for j in range(3):
            subarray.append(i)
        newarray.append(subarray)
    print(newarray)
#exam5()


