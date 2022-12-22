def typecontrole(a):
    if isinstance(a,int):
        print("integer")
    if isinstance(a,float):
        print("float")
    if isinstance(a,str):
        print("string")
    else:
        print("iets anders")


n="test"
typecontrole(n)
