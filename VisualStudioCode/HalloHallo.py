from random import random,randint,seed 
print(random())
seed()
print( "Een toevalsgetal tussen 1 en 10 is", randint( 1, 10 ) )
print( "Een ander is", randint( 1, 10 ) )
seed( 1 )
print( "3 seed toevalsgetallen zijn:", random(), random(), random() )
seed( 1 )
print( "Dezelfde 3 zijn:", random(), random(), random() )