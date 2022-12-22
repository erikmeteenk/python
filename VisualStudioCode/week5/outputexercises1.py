def exercise1():
    a = "5"
    b = 3
    print("I want", a, "puppies and"+b, "cats")#+ kan niet gebruikt worden tussen str en int
#exercise1()
def exercise2():
    print(f"{(41+200) % 24}:00")
#exercise2()
def exercise3():
    a = input("give a number:")
    print(a)
#exercise3()
def exercise4():
    a = input("voornaam:")
    b = int(input("age:"))
    print(a + b)
#exercise4()
def exercise5():
    amount = 99
    a = amount // 15
    b = amount % 15
    c = a // 3
    d = b % 3
    print(a,b,c,d)
#exercise5()
def exercise6():
    answer = input("enter a string:")
    print(len(answer))
#exercise6()
def exercise7():
    score = int(input("geef score:"))
    if score <= 30:
        letter_grade = "max score"
    elif score >= 15:
        letter_grade = "You just passed"
    else:
        letter_grade = "Failed!"
    print(letter_grade)
#exercise7()
def exercise8():
    number = int(input("number:"))
    if number == 10:
        print("A")
    if number < 30:
        print("B")
    if number > 5:
        print("C")
    if number < 11:
        print("D")
    if number < 4:
        print("E")
#exercise8()
def exercise9():
    a = True
    b = False
    c = False
    if a or b and c:
        print("A")
    else:
        print("B")
#exercise9()
def exercise10():
    a = True
    b = False
    c = False
    if not a or b:
        print(1)
    elif not a or not b and c:
        print(2)
    elif not a or b or not b and a:
        print(3)
    else:
        print(4)
#exercise10()
def exercise11():
    count = 1
    for i in range(3):
        count += 1
    print(count)
#exercise11()
def exercise12():
    for i in range(3,10):
        j = i+2
        print(j)
#exercise12()
def exercise13():
    a = int(input("getal1"))
    b = int(input("getal2"))
    total = 0
    while a <= b:
        total +=a
        a += 1
    print(total)
#exercise13()
def exercise14():
    array = [1,6.0,"9",1.34,32]
    for i in array:
        if isinstance(i,int):
            print(i)
#exercise14()
def exercise15():
    a = []
    for i in range(5):
        a.append(i)
    b = []
    for i in range(7):
        if i in a and i%2 == 0:
            b.append(i)
    print(b)
#exercise15()
def exercise16():
    temp = ["Geeks","for","Geeks"]
    array = []
    for i in temp:
        array.append(i[0].upper())
    print(array)
#exercise16()
def exercise17():
    n = 5
    for i in range(n):
        for j in range(i):
            print("* ", end="")
        print("")
    for i in range(n,0,-1):
        for j in range(i):
            print("* ",end="")
        print("")
#exercise17()
def exercise18():
    array = []
    for i in range(3):
        sarray = []
        for k in range(3):
            sarray.append(i)
        array.append(sarray)
    print(array)
#exercise18()
def exercise19(array2D,getal):
    for i in array2D:
        for k in i:
            if k % getal == 0:
                print(k)
a = [[1,2,3],[12,9,45]]
b = 3
#exercise19(a,b)
def exercise20(b):
    newarray = []
    for i in b:
        sarray = []
        for k in i:
            if k != 10:
                sarray.append(k)
        newarray.append(sarray)
    print(newarray)
a = [[1,2,4,58],[3,10,5,12],[3,4,10,52]]
#exercise20(a)






