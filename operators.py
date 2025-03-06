#Arithmetic operators
#a+b, a-b, a*b, a/b, a//b, a%b, a**b

#comparison operators
# x==y, x!=y, x<y, x>y, x<=y, x>=y

#Logical opeartors
# x and y, x or y, not x

#membership opeartors
#in, not in

#identity opeartors
#is, ==, is not

#bitwise operators
#a&b, a|b, a^b, ~a, a<<1, a>>1


x = 8
y = 3
print(x % y)
print(x > 5 and y < 5)
print(x | y)


nums = [10,20,30]
print(20 in nums)
print(50 not in nums)

#is - checks if two variables referes to the same memory location
#== - checks if 2 variables have the same value
 
x = 'Hello'
y = 'Hello'
print(x is y)

#Python optimizes memory by resuing these same objects for Immutable objects(strings,tuples,integers,etc.)

a = [1,2,3]
b = [1,2,3]
print(a is b)

#Python creates 2 different objects in memory eventhough mutable objects have same values.
