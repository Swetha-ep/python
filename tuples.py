# A tuple is an ordered, immutable collection of items. Unlike lists, tuples cannot be modified after creation.
# Tuple with multiple values
numbers = (1, 2, 3, 4, 5)
print(numbers)  # (1, 2, 3, 4, 5)

# Tuple with different data types
info = ("Alice", 25, True)
print(info)  # ('Alice', 25, True)

# Single-element tuple (comma is required)
single = (42,)
print(single)  # (42,)

# accessing
colors = ("red", "green", "blue")

print(colors[0])   # red
print(colors[-1])  # blue

# slicing
print(colors[0:2])  # ('red', 'green')


# packing and unpacking
# Packing a tuple
person = ("John", 30, "Engineer")

# Unpacking a tuple
name, age, job = person
print(name)  # John
print(age)   # 30
print(job)   # Engineer

t = 1, 2, 3  # No need for parentheses
print(t)  # Output: (1, 2, 3)
a, b, c = t  # Unpacks tuple values into variables
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


a, *b = t
print(a)  # 10
print(b)  # [20, 30]  (b gets the rest as a list!)


# tuples are immutable
nums = (1, 2, 3)
nums[0] = 10  # ❌ ERROR! Tuples cannot be modified.


# tuple methods
numbers = (1, 2, 3, 4, 2, 2)

print(numbers.count(2))  # 3 (Counts occurrences of 2)
print(numbers.index(4))  # 3 (Index of value 4)


# Use Tuples when:

# You want to store fixed data (e.g., months of the year).
# You need faster access (tuples are slightly faster than lists).
# You want to ensure data remains unchanged (immutability)
# Used as Dictionary Keys (since they're hashable).
data = {(1, 2): "Point A", (3, 4): "Point B"}
print(data[(1, 2)])  # Output: "Point A"


# concatenation
a = (10, 20, 30)
b = (40, 50)
c = a + b
print(c)
print(len(c))

# output 
# (10, 20, 30, 40, 50)
# 5



