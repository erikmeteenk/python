n = int(input("geef een getal in:"))
x = 0
y = 1
print(x)
print(y)
for i in range(n-1):
    z = x + y
    print( z)
    x = y
    y = z    