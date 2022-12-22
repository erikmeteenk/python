x = input("voer getal in:")
y = len(x)
x = int(x)
z = int(y*2)
if y < 2:
    z = int(y*2+1)
v = "|"
w = z+1
#print("{:>{z}}".format(" |",z=z),end="")
#print( "    |", end="" )
print(f"{v:>{w}}", end="")
for i in range( 1, x+1 ):
    print(f"{i:>{z}}",end="")
    #print( "{:>{z}}".format( i,z=z ), end="" )
print()
for i in range( (x*z)+(z+1) ):
    print( "=", end="" )
print()
for i in range( 1, x+1 ):
    print("{:>{z}}".format(i,z=z),end=""), print(  "|", end="" )
    for j in range( 1, x+1 ):
        print( "{:>{z}}".format( i*j,z=z ), end="" )
    print()