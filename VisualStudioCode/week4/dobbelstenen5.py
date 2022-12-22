from random import randint
n = int(input("voer het aantal dobbelstenen in:"))
pogingen = 100000#= int(input("voer aantal pogingen in:"))
success = 0
for i in range (pogingen):
    x = 0
    for j in range(n):
        z = randint(1,6)
        if z < x:
            break
        x = z
    else:
        success +=1
        
print("probabiliteit:",success/pogingen)

