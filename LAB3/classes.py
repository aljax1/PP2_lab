class xclass:
    def getString(self):
        self.text = input()
    
    def printString(self):
        print(self.text.upper())


obj = xclass()
obj.getString()
obj.printString()




class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

print(Shape().area())       

print(Square(10).area()) 






class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width


print(Rectangle(5, 3).area())





import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
p1 = Point(3, 4)
p2 = Point(7, 1)

p1.show()  
p2.show()  

p1.move(5, 6)
p1.show() 

print("Distance between points:", p1.dist(p2))  






numbers = [1, 2, 3, 4, 5, 10, 13, 17, 18, 19, 23, 24, 29, 35, 40]

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)
