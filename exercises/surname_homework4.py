# Surname
# Control flows

import random

def is_prime(n):
    if n > 1:
        # check for factors
        for i in range(2,n):
            if (n % i) == 0:
                return False
        else:
            return True
    return False

# Use l1 for the following questions
# creates a list of 50 random number
l1 = random.sample(range(-100, 100), 50)


# Create a while loop and a for loop that prints all the odd numbers from l1
print("Question 1")
# While loop
i = 0
while i < len(l1):
    if l1[i] % 2 != 0:
        print(l1[i], end = " ")
    i += 1

# For loop
for x in l1:
    if x % 2 != 0:
        print(x, end = " ")

# Create a while loop and a for loop that 
# prints all the non-negative prime numbers.
# Use the function "is_prime(n)" to check if the number is prime
print("Question 2")
# While loop
i = 0
while i < len(l1):
    if l1[i] > 0 and is_prime(l1[i]):
        print(l1[i], end = " ")
    i += 1

# For loop
for x in l1:
    if x > 0 and is_prime(x):
        print(x, end = " ")
    i += 1


# Use the seating_arrangement variable
seating_arrangement = [
    ["almeyda", "avilledo", "bajar", "cuadra"],
    ["deguzman", "deocampo", "durana", "eclarin"],
    ["formanes", "mabilin", "mabunga", "oabel"],
    ["pajarillo", "pabilonia", "palines", "quinto"],
    ["rea", "rubio", "tabarina", "zarsuelo"]
]

# Using a while loop within a while loop,
# print all the students at the back of "avilledo"
# Hint, take a not of the index and counter variable.
# You can use this to check which column you are in.
print("Question 3")
i = 0
j = 0
while i < len(seating_arrangement):
    while j < len(seating_arrangement[i]):
        if j == 1:
            print(seating_arrangement[i][j])
            break
        j += 1
    i += 1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using the nums variable, print out a multiplication table.
# The output should be silimar to this

# 1 2 3 4 5 6 7 8 9 10 
# 2 4 6 8 10 12 14 16 18 20 
# 3 6 9 12 15 18 21 24 27 30 
# 4 8 12 16 20 24 28 32 36 40 
# 5 10 15 20 25 30 35 40 45 50 
# 6 12 18 24 30 36 42 48 54 60 
# 7 14 21 28 35 42 49 56 63 70 
# 8 16 24 32 40 48 56 64 72 80 
# 9 18 27 36 45 54 63 72 81 90 
# 10 20 30 40 50 60 70 80 90 100

# Use a for loop within a for loop to do this.
# Hint, always use different counter variables on different loops
print("Question 4")
for x in nums:
    for y in nums:
        print(x * y, end=" ")
    print("")



# Given variable "cnt", create the image bellow. 
# "cnt" can be any value from 3 - 10
# cnt = 5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# cnt = 3
#   *
#  * *
# * * *
#  * *
#   *
cnt = 5
print("Question 5")

i = 0
j = 0
while i < (cnt * 2) - 1:
    while j < cnt:
        if j >= (i - (cnt - 1) if i >= cnt else (cnt - 1) - i):
            print("* ", end="")
        else:
            print(" ", end="")
    
        j += 1
    
    print("")
    j = 0
    i += 1

i = 0
j = 0
while i < cnt:
    while j < cnt:
        if j >= ((cnt - 1) - i):
            print("* ", end="")
        else:
            print(" ", end="")
    
        j += 1
    
    print("")
    j = 0
    i += 1

# BONUS QUESTION
# 100 php load for the first THREE correct answer

# Draw this image using the same "cnt" variable

# cnt = 5
#           * *
#         * * * *
#       * *     * *
#     * *         * *
#   * *             * *
# * *                 * *
#     * * * * * * * *
#       * * * * * *
#         * * * *
#           * *     
















