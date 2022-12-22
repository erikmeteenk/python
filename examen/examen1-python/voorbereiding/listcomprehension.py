"""Een list comprehension bestaat uit een expressie tussen vierkante haken, 
bestaande uit een for statement, gevolgd door nul of meer for en/of if statements. 
Het resultaat is een list die de elementen bevat die het resultaat zijn van 
de evaluatie van de combinatie van de for en if statements."""

data = [x for x in range(5)]
temp = [x for x in range(7) if x in data and x % 2 ==0]
print(temp)