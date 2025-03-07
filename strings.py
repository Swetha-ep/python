#indexing (Character accessing)
text1 = 'Python'

print(text1[0])
print(text1[-2])


#slicing : string[start:end:step]
print(text1[0:4])
print(text1[:4])
print(text1[2:])
print([text1[::2]])
print(text1[::-1])


text = "hEllo WoRLd"

print(text.lower())  # hello world (Converts to lowercase)
print(text.upper())  # HELLO WORLD (Converts to uppercase)
print(text.title())  # Hello World (Capitalizes first letter of each word)
print(text.capitalize())  # Hello world (Capitalizes first letter of the string)


text = "  Python  "

print(text.strip())   # "Python" (Removes spaces from both sides)
print(text.lstrip())  # "Python  " (Removes spaces from left)
print(text.rstrip())  # "  Python" (Removes spaces from right)


text = "Python is fun"

words = text.split()  # Splits string into a list
print(words)  # ['Python', 'is', 'fun']

sentence = "-".join(words)  # Joins list into a string with "-"
print(sentence)  # Python-is-fun


text = "I love Python"

print(text.find("Python"))  # 7 (Returns index of first occurrence)
print(text.replace("Python", "Django"))  # "I love Django"


text = "  Hello Python   "
print(text.strip().upper().replace('PYTHON','Django'))



#string formatting

#fstrings

name = "Swetha"
age = 25

print(f"My name is {name} and I am {age} years old.")

print(f"Next year, I will be {age + 1} years old.")


#.format()
name = "Swetha"
age = 25

print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))
print("My name is {name} and I am {age} years old.".format(name="Swetha", age=25))


#old style like c language
name = "Swetha"
age = 25

print("My name is %s and I am %d years old." % (name, age))

pi = 3.14159
print("Pi value: %.2f" % pi)  # Pi value: 3.14


fruit = "apple"
quantity = 5
print(f'I bought {quantity} {fruit}s today!')


#escape sequences
print("Hello\nPython")
print("name:\tSwetha")
print('It\'s a beautiful day!')
print("He said \"Hello\"")
print("This is a backslash: \\")


print("Python\n\tis\n\t\tawesome!")


#Immutable
#cannot assign directly like text[0] = "M" - causes an error
#TypeError: 'str' object does not support item assignment

text2 = "Hello"
new_text = "M" + text2[1:]
print(new_text)


#.replace()
text3 = "Python"
text3 = text3.replace("P","J")
print(text3)


word = "Django"
word = "F" + word[1:]
print(word)


#memory location difference
word1 = "Python"
print(id(word1))

word1 = "Jython"
print(id(word1))


#Garbage Collector in python
a = "Hello"
b = a  # Both 'a' and 'b' refer to "Hello"

a = "Mello"  # Only 'a' changes; 'b' still points to "Hello"
print(b)  # "Hello" is still in memory because 'b' uses it!

#Python only removes an object when nothing references it.