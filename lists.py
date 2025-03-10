#A list is an ordered, mutable collection of elements.
# Empty list
my_list = []
# List with numbers
numbers = [1, 2, 3, 4, 5]
# List with mixed data types
mixed = [10, "hello", 3.14, True]
# Nested lists
nested = [[1, 2], [3, 4], [5, 6]]


#accessing
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (negative index = last item)


#slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40] (index 1 to 3)
print(numbers[:3])   # [10, 20, 30] (first 3 elements)
print(numbers[2:])   # [30, 40, 50] (from index 2 to end)


#modifying
#1 changing
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"   # Change "banana" to "orange"
print(fruits)  # ['apple', 'orange', 'cherry']

#2 adding
fruits.append("grape")      # Add to the end
fruits.insert(1, "mango")   # Insert at index 1
print(fruits)  # ['apple', 'mango', 'orange', 'cherry', 'grape']

#3 removing
fruits.remove("cherry")  # Remove by value
fruits.pop(1)            # Remove by index
del fruits[0]            # Delete an element
fruits.clear()           # Remove all elements


#list operations
#concatenation and repitition
list1 = [1, 2, 3]
list2 = [4, 5]

print(list1 + list2)  # [1, 2, 3, 4, 5] (concatenation)
print(list1 * 3)      # [1, 2, 3, 1, 2, 3, 1, 2, 3] (repetition)

#2 checking membership
numbers = [10, 20, 30]
print(20 in numbers)   # True
print(40 not in numbers)  # True

#3 iterating 
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#other methods
#.index(x)
# .count(x)
# .sort()
# .reverse()
# .copy()


#list comprehension
# Using a for loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Using list comprehension (same output in one line)
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Get even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

#map()
numbers = [1,2,3,4,5]
squared = list(map(lambda x:x**2,numbers))
print(squared)

#filter()
num = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0,num))
print(even)

#nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[0])    # [1, 2, 3]
print(matrix[1][2]) # 6 (row index 1, column index 2)

# Flattening a Nested List using List Comprehension
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#sorting
#1
numbers = [5, 2, 9, 1, 7]
print(sorted(numbers))  # [1, 2, 5, 7, 9]

#2
words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['kiwi', 'apple', 'cherry', 'banana']

#3
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(4, 1), (2, 2), (1, 3)]



