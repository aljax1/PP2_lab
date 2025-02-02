def grams_to_ounces(grams):
    return 28.3495231 * grams
grams = int(input())
print(grams_to_ounces(grams))


def fahrenheit_to_centigrade(F):
    return (5 / 9) * (F - 32)
F=int(input())
print(fahrenheit_to_centigrade(F))




def solve(numheads,numlegs):
    rabbits = (numlegs - 2 * numheads)//2
    chicken = numheads - rabbits
    return (chicken, rabbits)  
print(solve(35,94))  


def filter_prime(numbers):
    primes = []
    for num in numbers:
        check = 0
        for i in range(2, num):
            if num % i == 0:
                check += 1
        if check == 0 and num > 1:
            primes.append(num)
    return primes
user_input = input()
numbers = [int(n) for n in user_input.split()]

print("Prime numbers:", filter_prime(numbers))




def reverse_sentence(s):
    words = s.split()  
    reversed = words[::-1]  
    return ' '.join(reversed) 
user = input()
result = reverse_sentence(user)
print(result)


def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == 3 and nums[i-1] == 3:
            return True
    return False
List = input()
numbers = list(map(int,List.split()))
print(has_33(numbers))



def spy_game(nums):
    step = 0
    for num in nums:
        if step == 0 and num == 0:
            step = 1
        elif step == 1 and num == 0:
            step = 2
        elif step == 2 and num == 7:
            return True
    return False
print(spy_game([1,7,2,0,4,5,0]))




import math
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)
a = int(input())
print(sphere_volume(a))




def unique_list(input_list):
    unique_elements = []
    for item in input_list:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements
a = input()
list = list(map(int,a.split()))
print(unique_list(list))


def is_palindrome(s):
    processed = s.replace(" ", "").lower()
    return processed == processed[::-1]

user_input = input("Enter : ")
if is_palindrome(user_input):
    print("This is a palindrome")
else:
    print("not palindrome")






def histogram(numbers):
    for num in numbers:
        print('*' * num)

numbers = list(map(int, input("Enter : ").split()))
histogram(numbers)



import random

print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
secret_num = random.randint(1, 20)
guesses_taken = 0

while True:
    print("Take a guess.")
    guess = int(input())
    guesses_taken += 1
    
    if guess < secret_num:
        print("Your guess is too low.")
    elif guess > secret_num:
        print("Your guess is too high.")
    else:
        break  

print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")