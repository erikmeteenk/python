
lijst = ["appel", "banaan", "kers", "doerian", "mango"]
print(len(lijst))
i = 0
for i in range(0,len(lijst)):
     x = lijst[i].upper()
     lijst.append(x)
     del lijst[0]
print(lijst)
lijst.reverse()
print(lijst)