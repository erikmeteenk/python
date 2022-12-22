#invoer = [3,3,23,42,13,2,100,97,1,42]
invoer = []
x = int(input("voer het aantal series in:"))
invoer.append(x)
for aantx in range(1,x+1):
	y = int(input(f"voer de lengte van serie {aantx} in:"))
	invoer.append(y)
	for aanty in range(1,y+1):
		z = int(input(f"voer getal {aanty} van serie {aantx} in:"))
		invoer.append(z)
k = invoer[0]
npos = 1
print(invoer)
for i in range(1,k + 1):
	n = invoer[npos]
	sarray= []
	for j in range(1,n+1):
		sarray.append(invoer[npos + j])
	print(i, end=' ')
	print(min(sarray),end=' ')
	print(max(sarray))
	npos= (npos + n + 1)