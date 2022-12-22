

def convert_cel_to_far(temp_cel):
    """Return the Celsius temperature temp_cel converted to Fahrenheit.Dit is ongeveer de formule: 
    1 graad Fahrenheit is ongeveer 0,56 graad Celsius. 0C komt overeen met 32F."""
    fahrenheit = (temp_cel/0.6)
    print(fahrenheit)
#convert_cel_to_far(30)

def convert_far_to_cel(temp_far):
    """Return the Fahrenheit temperature temp_far converted to Celsius."""
    celcius = (temp_far*0.6)
    print(celcius)
#convert_far_to_cel(50) 


# Prompt the user to input a Fahrenheit temperature.
"""write code here"""
invoer = float(input("input a Fahrenheit temperature:"))


# Convert the temperature to Celsius.
convert_far_to_cel(invoer) 
# Note that `temp_far` must be converted to a `float`
# since `input()` returns a string.
"""write code here"""


# Display the converted temperature
"""write code here"""


# You could also use `round()` instead of the formatting mini-language:
# print(f"{temp_far} degrees F = {round(temp_cel, 2)} degrees C"")
"""write code here"""

# Prompt the user to input a Celsius temperature.
"""write code here"""
invoer2 = float(input("input a celcius temperature:"))
# Convert the temperature to Fahrenheit.
"""write code here"""
convert_cel_to_far(invoer2)
# Display the converted temperature
"""write code here"""
