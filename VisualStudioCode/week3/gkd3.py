import math
grootste=0
kleinste=math.inf
drievouden=0

for i in range (1,11):
    x=int(input(f"voer getal {1} in:"))
    if grootste == 0:
        grootste = x
    if kleinste == 0:
        kleinste == x

    if x % 3 == 0:
        drievouden +=1

    if grootste < x:
        grootste = x
    if kleinste > x:
        kleinste = x
        
print("grootste:", grootste)
print("kleinste:", kleinste)
print("drievouden:", drievouden)