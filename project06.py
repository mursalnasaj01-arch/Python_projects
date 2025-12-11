# Area of a regular polygon
import math

# request for the side and length of polygon
n=int(input("Please enter the numberof the side: "))
s=int(input("please enter the length of the side: "))

area=(n*s**2)/(4*math.tan(math.pi/n))

# result
print(f"The area of the polgon is: {area:.2f}")