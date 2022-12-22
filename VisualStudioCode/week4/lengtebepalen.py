x = input("voer getal in:")
y=len(x)
print(x)
print(y)
z = int(y*2+1)
print(z)
for i in range (10):
	print("{:>{z}}".format(i,z=z),end="")