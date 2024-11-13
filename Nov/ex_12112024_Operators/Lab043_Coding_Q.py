# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)

import math
# Logic Building Formula

# || Step 1 ||
# Figure out the inputs and output
# input -> r ->  data type -> float
# pi = 3.14
# power -> pow or ** -> any
# o/p -> float - area , print area


# || Step 2 ||
# rough logic =  area = 3.14 * pow(r,2)

# || Step 3 ||
radius = float(input("enter the radius if the circle\n"))
print(radius)
print(math.pi)
#area = 3.14 * (radius**2)
#area = (math.pi) * (radius**2)
area = math.pi * math.pow(radius,2)
print("area of the circle is" ,area)
print(f"area of the circle is {area:.3f}")

print(math.pow(11,2))

print(3.14 * float(input("enter the radius if the circle\n"))**2)

print(math.asin(90))
