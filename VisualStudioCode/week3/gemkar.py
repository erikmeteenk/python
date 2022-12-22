lijn1=input("eerste lijn:")
lijn2=input("tweede lijn:")
lijn3=""
teller=0
for i in (lijn1):
    for j in (lijn2):
        if i == j:
            if j in (lijn3):
                continue
            lijn3 += i
            teller +=1

print(lijn3)