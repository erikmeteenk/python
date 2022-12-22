n = int(input("voer waarde m in:"))
m = int(input("voer waarde n in:"))
teller  = 0

    #n=int(input("voer een nieuwe waarde in voor n want vorige n > m:"))
for i in range (m):
    if n > m:
        break
    for j in range(m):
        if (i**2+j**2 ) > m or (i**2+j**2 ) < n:
            continue
        print(f"{i} ** 2 + {j} ** 2 = {i**2+j**2}")
        teller +=1
