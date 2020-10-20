# Problem 1.2 

# Goal is to "return the integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b."

import math

def get_hypotenuse(a,b):

    a = int(input("Type A-val here --> "))
    b = int(input("Type B-val here --> "))

    c = a**2+b**2
    hypotenuse = math.sqrt(c)
    return hypotenuse

print(get_hypotenuse(1,1))