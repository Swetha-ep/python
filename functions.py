def greet():  
    print("Hello, Swetha!")  

greet()  # Calling the function


#arguments and parameters
def greet(name):  
    print(f"Hello, {name}!")  

greet("Kiki")  # Output: Hello, Kiki!


#return 
def add(a, b):  
    return a + b  

result = add(5, 3)  
print(result)  # Output: 8


#Types of arguments
#1 positional
def info(name, age):  
    print(f"Name: {name}, Age: {age}")  

info("Swetha", 22)  # Correct order
info(22, "Swetha")  # Wrong order! (Age and name swapped)


#2 keyword
info(age=22, name="Swetha")  # Order doesn't matter now!


#3 default
def greet(name="Guest"):  
    print(f"Hello, {name}!")  

greet()         # Output: Hello, Guest!  
greet("Swetha") # Output: Hello, Swetha!



#4 variable length (*args,**kwargs)
def add_numbers(*args):  #in tuple style
    return sum(args)  

print(add_numbers(1, 2, 3, 4))  # Output: 10  

def display_info(**kwargs):  #in dictionary style
    for key, value in kwargs.items():  
        print(f"{key}: {value}")  

display_info(name="Swetha", age=22, city="Chennai")  


#lamda functions
add = lambda x, y: x + y  
print(add(5, 3))  # Output: 8


def multiply(n):
    return lambda x: x * n  

double = multiply(2)  # Function that doubles a number
print(double(5))      # Output: 10



#map()
#map(function, iterable)
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]


#filter()
#filter(function, iterable)
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]


#sorted()
#returns a new sorted list
words = ["banana", "apple", "cherry", "kiwi"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['kiwi', 'apple', 'banana', 'cherry']


numbers = [3, 1, 4, 1, 5, 9]
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)  # Output: [9, 5, 4, 3, 1, 1]


#sort()
#only for lists
#modifies the list in place
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()  # Sorts in-place
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]


numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]


#Recursion
def factorial(n):   #formula - n!=n×(n−1)×(n−2)×...×1
    if n == 0:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120


#formula - F(n)=F(n−1)+F(n−2)
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0  # First Fibonacci number
    elif n == 2:
        return 1  # Second Fibonacci number
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 5


#exercise 1
def sum_digits(n):
    if n < 10:
        return n
    return n%10 + sum_digits(n//10)

print(sum_digits(123)) 


#exercise 2
def reverse(word):
    if len(word) == 1:  # Base case: If only one character, return it
        return word
    return word[-1] + reverse(word[:-1])  # Recursive step

# Test cases
print(reverse("hello"))  # Output: "olleh"
print(reverse("python"))  # Output: "nohtyp"


#exercise
#fibonacci
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))


#palindrome
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome("madam"))


#power of a number
def power(a,b):
    if b == 0:
        return 1
    return a * power(a, b-1)

print(power(2,3))