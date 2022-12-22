def pythagoras(a,b):
    from math import sqrt
    if a<=0 or b<=0:
        return -1
    return sqrt(a*a+b*b)

print(pythagoras(2,4))
