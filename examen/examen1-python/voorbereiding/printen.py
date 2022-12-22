print("a","b","c","d")
print("a"),print("b"),print("c"),print("d")
print("a",end=""),print("b",end=""),print("c",end=""),print("d")
print(("a","b","c","d"))
list = [1,2,3,4]
print(list)
for i in list:
    print(i)
for i in list:
    print(i,end="")
print()
for i in range(len(list)):
    print(i,end="")   
print()
print(f"dit is een lijst {list}")
print()
print(list[-2:])
print(list[1:])
