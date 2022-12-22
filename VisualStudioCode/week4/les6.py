#array kan verschillende datatypes bevatten
array = ["Ford", "Mustang", 1964 ]

#delete element uit array gebaseerd op index
def del_element_array_index():
    array.pop(0)
    print(array)

#delete element uit array gebaseerd op value
def del_element_array_value():
    a = ["ser","hat"]
    a.remove("hat")
    print(a)


#dictionary met key:value pair
dictionary = {
            1: "voornaam",
            2: "Achternaam",
            3: "leeftijd"
            }

#een nieuw element toevoegen aan een dictionary
dictionary[4] = "serhat"
print(dictionary)

#loopen over een dictionary
def loop_dictionary():
    for k,v in dictionary.items():
        print(k,v)

#element deleten uit een dictionary
def del_element_dictionary():
    del dictionary[1]
    print(dictionary)

#2d array (matrix)
array = [[1,2,4,58 ], 
         [3,4,5,12], 
         [3,4,5,52]]

def loop_2d_array():
    for i in array: # array = [[1,2,4,58 ], [3,4,5,12], [3,4,5,52]]
        for k in i: # i = [1,2,4,58 ]
            print(k)

#functie1: Schrijf een functie die 2 argumenten 
# verwacht. Beiden argument zijn arrays. 
#print elke element uit behavle het getal 10
def functie1(arg1,arg2):
    for i in arg1:
        if i != 10:
            print(i)
    for i in arg2:
        if i != 10:
            print(i)

a = [1,10,3]
b = [1,10,3]

functie1(a,b)

#functie2: schrijf een functie die 1 argument
#verwacht. Deze argument is een 2d-array. Je 
#delete alle getallen met waarden 10.

def functie2(b):
    newArray = []                # newArray = []
    for i in b:                  # i = [1,2,4,58 ]
        sArray = []              # sArray = []
        for k in i:              # k = 1
            if( k !=10):         # true
                sArray.append(k) # sArray = [1,2,4,58 ]
        newArray.append(sArray)

a =     [[1,2,4,58 ], 
         [3,10,5,12], 
         [3,4,10,52]]

functie2(a)