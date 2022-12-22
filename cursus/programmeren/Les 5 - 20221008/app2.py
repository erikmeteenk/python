#String -> text
#int -> geheel getal
#float -> komma getal
#boolean -> true or false

x = "5"
y = 5
z = 5.0


def print_leeftijd(a,b):
    #leeftijd = int(input("leeftijd: "))
    print(a)
    print(b)


def old_enough_to_drive(leeftijd):
    if leeftijd > 18:
        print("oud gng om te rijden")
    else:
        print("mag nog niet rijden")

def calc_sqrt(getal):
    x = math.sqrt(getal)
    print(x)

k = int(input("leeftijd: "))
z = int(input("lengte: "))

print_leeftijd(k,z)
old_enough_to_drive(k)




