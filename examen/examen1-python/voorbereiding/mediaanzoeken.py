# print(7/2)
# print(round(7/2))
# print(int(7//2))
def mediaan_zoeken(reeks):
    reeks.sort()
    if len(reeks) % 2 == 1:
        mediaan = reeks[round((len(reeks)/2)-1)]
        
    elif len(reeks) % 2 == 0:
        mediaan = (reeks[(len(reeks)//2)-1] + reeks[(len(reeks)//2)])/2
    print(mediaan)
   
    print(reeks)
#a = [ 45,60,89,78,10]
a = [ 45,60,89,78,85,10,30,78,56,45]
mediaan_zoeken(a)

def mediaan_zoeken2(reeks):
   from statistics import median
   mediaan = median(reeks)
   print(mediaan)
   print(reeks)    
#a = [ 45,60,89,78,10]
a = [ 45,60,89,78,85,10,30,78,56,45]
mediaan_zoeken2(a)