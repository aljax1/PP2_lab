#1
import math
degree = float(input("Input degree: "))
radian  = degree*math.pi/180
print(f"Output radian: {radian:.6f}")


#2
import math
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
area = (a+b)*h/2
print(f"Expected Output: {area}")


#3
import math

n=int(input("Input number of sides: "))
a=int(input("Input the length of a side: "))
area = int((n * a**2) / (4 * math.tan(math.pi / n)))

print("The area of the polygon is: ",area)


#4
import math

b=int(input("Length of base: "))
a=int(input("Height of parallelogram: "))

print(f"Expected Output: {float(a*b)}")