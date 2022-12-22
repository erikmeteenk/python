def del7not5():
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i,end=",")
#del7not5()

print()

# data = [x for x in range(2000,3201) if x % 7 == 0 and x % 5 != 0]
# print(data)

# Define a Python function which can generate and print a list where the values are square of
# numbers between 1 and 20 (both included
def squarevalues():
    newlist = []
    for i in range(1,21):
        x = i**2
        newlist.append(x)
    print(newlist)
#squarevalues()

#Write a Python function that adds the outer values of the matrix together.

def rondomoptellen(reeks):
    som = 0
    for i in range(len(reeks)):
        if i != 0 and i != (len(reeks)-1):
            
            x = (reeks[i][0]+reeks[i][-1])
            som += x
        else:
            x = (sum(reeks[i]))
            som += x
    print(som)



reeks = [ [ 12 , 12 , 12 , 13 ] ,
          [ 43 , 43 , 43 , 54 ] ,
          [ 44 , 44 , 44 , 23 ] ,
          [ 99 , 34 , 12 , 12 ] ,

]
#rondomoptellen(reeks)

        
    

