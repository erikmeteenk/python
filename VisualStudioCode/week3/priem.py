getal = int(input("getal invoeren:"))
test = 0
for i in range(1,getal):
    if (getal % i) == 0:
        
        if i != 1 and i != getal:
            test = 0
        else:
            test = 1
if test == 1:
    print(f"{getal} is een priemgetal!")
else:
    print(f"{getal} is geen priemgetal!") 