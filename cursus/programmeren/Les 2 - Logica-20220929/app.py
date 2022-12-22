#int: integer (een getal)
#str: string (tekst die tussen aanhalingstekens staat)
# == : hiermee word vergeleken 
#elif : multiple conditions
#<= of >=

def check_old_enough_to_drive():
    x = input("geef een getal: ")
    if  int(x) >= 17:
        print("your old enough for you driver license")
    else: 
        print("Your not old enough")

def som():
    x, y = input("geef getallen in: ").split()
    x = input("geef getallen in: ")
    y = input("geef getallen in: ")

    z = int(x) + int(y)
    print(z)

def avg_three_number():
    x, y, z = input("geef getallen in: ").split()
    k = (int(x) + int(y) + int(z))/3
    print(round(k))

def surfaceTraingle():
    x, y = input("geef getallen in: ").split()
    k = (int(x) * int(y))/2
    print(round(k))

def volumeCube():
    x = input("geef getal in: ")
    k = (int(x) * int(x) * int(x))
    print(k)

def lastTwoDigitsOfInteger():
    x = input("geef getal in: ")
    print(x[-2:])

som()
