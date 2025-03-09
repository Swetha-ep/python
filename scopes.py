# There are four types of scopes in Python (LEGB Rule):
# 1 Local Scope (Inside a function)
# 2 Enclosing Scope (Nested functions)
# 3 Global Scope (Declared at the top level)
# 4 Built-in Scope (Python’s built-in functions like print())


#local
def my_func():
    x=10
    print(x)

my_func()


#global
y=5
def myfunc2():
    print(y)

myfunc2()
print(y)


#enclosing
def outer_func():
    z=30

    def inner_func():
        print(z)

    inner_func()

outer_func()

#global keyword
count = 0
def func3():
    global count
    count += 1
    print("updated:",count)
func3()
print(count)
#By default, you cannot modify a global variable inside a function.
#Use global to explicitly modify it.


#non local
def outer():
    num = 5
    def inner():
        nonlocal num
        num += 1
        print("inner:",num)
    inner()
    print('outer:',num)
outer()


#built-in scope
# Python has many built-in functions like print(), len(), sum(), etc.
# Built-in functions exist in Python's memory before your program runs, so you can use them anytime. User-defined functions must be defined first before calling them.