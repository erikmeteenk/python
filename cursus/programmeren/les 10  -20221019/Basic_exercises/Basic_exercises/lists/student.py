# Exercise 1
# Create a list named food with two elements "rice" and "beans".
food = ["rice","beans"]
print(food)
# Exercise 2
# Append the string "broccoli" to the food list using .append()
food.append("broccoli")
print(food)
# Exercise 3
# Add the strings "bread" and "pizza" to food using .extend()
bb = ["bread","pizza"]
food.extend(bb)
print(food)
# Exercise 4
# Print the first two items in food using slicing notation
print(food[1:3])
# NOTE: The following is also acceptable


# Exercise 5
# Print the last item in food using index notation
print(food[-1])

# Exercise 6
# Create a list called breakfast from the string "eggs, fruit, orange juice"
breakfast = ["eggs", "fruit","orange juice"]

# Exercise 7
# Verify that breakfast has three items using len()
print (len(breakfast))

# Exercise 8
# Create a new list called `lengths` using a list
# comprehension that contains the lengths of each
# string in the `breakfast` list.
for i in range(len(breakfast)):
    x = len(i)
    