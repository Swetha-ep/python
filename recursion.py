# sum of digits of a number
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n//10)

print(sum_of_digits(1234))


# find maximum number in a tuple
def find_max(tup):
    if len(tup) == 1:
        return tup[0]
    return max(tup[0],find_max(tup[1:]))

tup = (4, 12, 8, 20, 6)
print(find_max(tup))