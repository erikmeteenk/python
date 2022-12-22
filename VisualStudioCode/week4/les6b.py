#array kan verschillende datatypes bevatten
array = ["Ford", "Mustang", 1964 ]
print(array) 
#delete element uit array gebaseerd op index
def del_element_array_index():
    array.pop(0)
    print(array)
del_element_array_index()