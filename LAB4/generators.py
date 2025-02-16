#1
def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

n = int(input("Enter a number = "))

for square in square_generator(n):
    print(square)


#2
def evens(n):
    for i in range(n + 1):  
        if i % 2 == 0:
            yield i

n = int(input("n = "))
print(", ".join(map(str, evens(n))))



#3
def d34(n):
    for i in range(n + 1): 
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("n = "))
print(list(d34(n)))  


#4
def squares(a, b):
    for i in range(a, b + 1): 
        yield i ** 2

a = int(input("a = "))
b = int(input("b = "))

for square in squares(a, b):
    print(square)



#5
def squares(a, b):
    for i in range(a, b + 1): 
        yield i ** 2

a = int(input("a = "))
b = int(input("b = "))

for square in squares(a, b):
    print(square)

    