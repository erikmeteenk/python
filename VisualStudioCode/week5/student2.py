list2 = ["Topol","Tipol"]
# Exercise 1
# Create an empty dictionary
dictionary = {}

# Exercise 2
# Add some key-value pairs to the dictionary

dictionary ["Enterprise"]=1
dictionary["Discovery"]=2

# Exercise 3
# Check if "Enterprise" and "Discovery" exist; if not, add them
dictionary ["Bedrijf"]=3
dictionary ["Ontdekking"]=4
print(dictionary)
# Bonus points: you could instead loop over a list of names to check
for i in list2:
    if i in dictionary:
        print ("yes", i)
print()

# Exercise 4
# Display the contents of the dictionary, one pair at a time
for key,value in dictionary.items():
    print(key,value)



# Exercise 5
# Remove "Discovery"
dictionary.pop("Discovery")
print(dictionary)
# Exercise 6 (Bonus)
# Create dictionary by passing a list to dict()
l1 = [1,2,3,4]
l2 = ["A","B","C","D"]
lijst = zip(l1,l2) #[(1,"A"), (2,"B")]
print(dict(lijst))


dictionary = dict([(1,"A"),(2,"B")])
