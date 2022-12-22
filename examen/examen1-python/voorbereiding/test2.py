reeks = [ [ 12 , 12 , 12 , 13 ] ,
          [ 43 , 43 , 43 , 54 ] ,
          [ 44 , 44 , 44 , 23 ] ,
          [ 99 , 34 , 12 , 12 ] ,

]
lijst = [ ("getal1",34) , ("getal2",14) ]
for i in reeks:
    for j in i:
        print(j)

print(lijst[1:3])

dictio = dict(lijst)
print(dictio)
dictio["getal3"]=16
print(dictio)
a = 15.0
print(type(a))

reekstup = tuple(reeks)
print(reekstup[1])

list2 = [reekstup]
list2.append([1,2,3,4])
print(list2)
reekstup = tuple(list2)
print(reekstup)