# Session 7
import random

# Global variable
l1 = random.sample(range(0, 100), 50)

def summation(lst):
    s = 0               # Local variable
    for i in lst:
        s += i
    return s

def count_me(n):
    for i in range(n):
        print(i, end=" ")

    print("")
    # Both loops count from 0 - n
    i = 0
    while i < n:
        print(i, end=" ")
        i += 1
    print("")

def multiplication(x, y):
    ans = 0

    for i in range(x):
        ans += y

    # i = 0
    # while i < y:
    #     ans += 4
    #     i += 1
    return ans

def exponent(x, y):
    # x ^ y
    # 4 ^ 0 --> 1
    ans = 1
    for i in range(y):
        ans *= x
        
    return ans

a, b = 4, 5
# print(multiplication(a, b))
# print(exponent(4, 2))
# count_me(5)


def fib(n):

    # 0 1 1 2 3 5 8 13 21 34 55 . . . . . . 
    first = 0
    second = 1
    n_val = 0 
    i = 0

    while i < n:
        if i <= 1:
            n_val = i  
        else:
            n_val = first + second
            first = second
            second = n_val
        print(n_val, end=' ')

        i += 1

    print('')

# fib(40)

# Recursion
# Function calling itself

# rsummation(5)
# 5 + rsummation(4) # 5 - 1
# 4 + rsummation(3) # 4 - 1
# 3 + rsummation(2) # 3 - 1
# 2 + rsummation(1) # 2 - 1
# 1
# 2 + 1             # rsummation(1)
# 3 + 3             # rsummation(2)
# 4 + 6             # rsummation(3)
# 5 + 10            # rsummation(4) 
# 15                # rsummation(5)

# rsummation(5) = 5 + rsummation(4)
# rsummation(5) = 5 + 4 + rsummation(3)
# rsummation(5) = 5 + 4 + 3 + rsummation(2)
# rsummation(5) = 5 + 4 + 3 + 2 + rsummation(1)
# rsummation(5) = 5 + 4 + 3 + 2 + 1
def rsummation(n):
    # Summation of numbers 1 - n
    # n = 5 = 1 + 2 + 3 + 4 + 5
    if n == 1 or n == 0:
        return 1
    return n + rsummation(n - 1)

print(rsummation(5))

def factorial(n):
    # 5! = 1 * 2 * 3 * 4 * 5
    # 10! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))


def fexponent(x, y):
    # x ^ y
    if y == 0:
        return 1
    if y == 1:
        return x

    return x * fexponent(x, y - 1)

print(fexponent(3, 3))

