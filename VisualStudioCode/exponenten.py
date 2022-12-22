from math import exp
f="{} {} {:2d} {} {:>8.5f}"
print(f.format("e", "**",-1, "=" ,exp(-1))) 
print(f.format("e", "**", 0, "=" ,exp(0))) 
print(f.format("e", "**", 1, "=" ,exp(1)))
print(f.format("e", "**", 2, "=" ,exp(2)))
print(f.format("e", "**", 3, "=" ,exp(3))) 