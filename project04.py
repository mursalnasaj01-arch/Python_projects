# Cylinder Area and volume
import math
#Get input for radius and height
radius =float(input("enter the radius of the Cylinder: "))
height=float(input("enter the height of Cylinder: "))

Volume=math.pi*radius**2*height
surface=2*math.pi*radius**2+2*math.pi*radius*height

#display the result
print("Volume of the Cylinder is:",round(Volume,2))
print("surface area of the Cylinder is:",round(surface,2))