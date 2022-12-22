def getalgenerator():
    from random import randint
    nieuwelijst=[]
    for i in range (100):
        x = randint(0,1000)
        nieuwelijst.append(x)
    return nieuwelijst
    print(nieuwelijst)

getalgenerator()

