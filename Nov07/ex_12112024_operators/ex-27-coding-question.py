# calculate area of circle given its radius using the formula area = pi x rsquare
import math

radius = float(input("enter the radius of the circle \n"))
print(radius)
area = 3.14 * (radius ** 2)
print("area of the circle is :", area)
print(f"Area of the circle is : {area:.3f}")  # format : .3f -> in o/p 2 numbers after decimal
#print(math.pi)
# print(math.pow(radius,__y:2)
# area1 = math.pi * math.pow(radius, _y:2)
# print(area1)
#print(3.14 * (float(input("enter the radius of the circle \n")) ** 2)) #whole program in one code
