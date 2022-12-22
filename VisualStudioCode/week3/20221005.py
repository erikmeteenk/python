#dictionaries are used to store data values in key:value pairs
from array import array
#array = ["ford","mustang",1964]
dictionary = {1:"voornaam",2:"achternaam",3:"leeftijd"}
del dictionary[1]
print(dictionary[3])
print(dictionary)
#for i in array:
 #   print("m")
for k,v in dictionary.items():
    print(k,v)

array = [[1,2,4,58],[3,4,5,12],[3,4,5,52]]  #is eigenlijk een matrix
for i in array:
    for k in i:
        print(k)
#array.pop(0)
print(array)
