# Exercise 1
# Create a tuple "cardinal_numbers" with "first", "second" and "third"



cardinal_numbers = ("first","second","third")


# Exercise 2
# Display the second object in the tuple
print(cardinal_numbers[1])

# Exercise 3
# unpack the tuple into three string and display them
x = cardinal_numbers[0]
y= cardinal_numbers[1]
z = cardinal_numbers[2]
print(x)
print(y)
print(z)
for i in cardinal_numbers:
    print(f"cardinal{i}")

# Exercise 4
# Create a tuple containing the letters of your name from a string
x = "erik"
namelist = []
for i in x:
    namelist +=i
print(namelist)
my_name = tuple(namelist)
print(my_name)
# Exercide 5
# Check whether or not x is in my_name
for i in my_name:
    if i == "x":
        print("x gevonden in naam")
        break
    print("niet gevonden") 

# Exercise 6
# Create tuple containing all but the first letter in my_name
my_newname = tuple(my_name[:-1])
print (my_newname)
naam = tuple("dam")
lijsttuple = tuple("138(klm)7")
print(naam)
pos1,pos2,pos3 = naam
print(pos1)
print(pos2)
print(pos3)
print(lijsttuple)
