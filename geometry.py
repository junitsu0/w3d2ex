from math import pi
from math import sqrt

r = float(input("Enter the radius of the circle: "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c)