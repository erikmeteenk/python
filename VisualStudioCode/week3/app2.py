"""een functie die een lijst meekrijgt, over deze lijst loopt en checkt hoeveel getallen kleiner zijn dan 5 + print """
nrs =[1,2,3,4,5,6,7,8,9,12,2,3]

def kleinerdan(nrs,getal):
    cnt=0
    for i in nrs:
        if i<getal:
            cnt=cnt+1
    print(cnt)
kleinerdan(nrs,10)