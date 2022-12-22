


#invoer
"""aantroost = int(input("voer aantal roosters in:"))
invoer = []
invoer.append(aantroost)
for i in range(invoer[0]):
    subarray = []
    for j in range(1,6):
        x = input(f"voer rooster {j} van reeks {i+1} in:" ).split()
        for k in range(len(x)):
            if x[k] != ".":
                x[k] = int(x[k])
            #print(x[k])
            if x[k] == ".":
                x[k] = 0
        
        subarray.append(x)
    invoer.append(subarray)
print(invoer)"""
#a =[2, [[0, 5, 0], [0, 0, 7], [4, 0, 0], [9, 15, 21], [7, 20, 18]], [[9, 0, 0], [0, 7, 0], [0, 0, 1], [17, 15, 13], [23, 14, 8]]]
# 2
# . 5 .
# . . 7
# 4 . .
# 9 15 21
# 7 20 18
# 9 . .
# . 7 .
# . . 1
# 17 15 13
# 23 14 8

#uitvoering
invoer = [2,[[0,5,0], [0,0,7],[4,0,0],[9,15,21],[7,20,18]],[[9,0,0],[0,7,0],[0,0,1],[17,15,13],[23,14,8]]]#simulatie
reference = [1,2,3,4,5,6,7,8,9]#cijfers van 1 tot negen
for i in range(1,len(invoer)):
    subarray = []
    for j in range(3):
        x = invoer[i][j]
        for k in x:
            if k != 0:
                reference.remove(k)
    subarray.append(reference)
    break
    
print (subarray)