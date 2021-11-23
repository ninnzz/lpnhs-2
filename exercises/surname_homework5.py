# Surname
import random

# Use l1 in the following questions
l1 = random.sample(range(0, 100), 80)

# Complete the following functions.
# Do not use buit in min() and max() functions

def minimum(lst):
    # Iterate thru lst and
    # return the smallest element

    return

def maximum(lst):
    # Iterate thru lst and
    # return the maximum element

    return

    

# Pascal's triangle!
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# Create a function that returns the nth row
# of the triangle!
# pascals_triangle(5) should return [1, 4, 6, 4, 1]
# pascals_triangle(6) should return [1, 5, 10, 10, 5, 1]

def pascals_triangle(n):
    # return the nth row in list form.

    return []


# Use this list for the following questions
seating_arrangement = [
    ["almeyda", "avilledo", "bajar", "cuadra"],
    ["deguzman", "deocampo", "durana", "eclarin"],
    ["formanes", "mabilin", "mabunga", "oabel"],
    ["pajarillo", "pabilonia", "palines", "quinto"],
    ["rea", "rubio", "tabarina", "zarsuelo"]
]

random_numbers = [
    random.sample(range(0, 100), 10),
    random.sample(range(0, 100), 10),
    random.sample(range(0, 100), 10)
]


# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# will be converted to
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

def custom_flatten(lst):
    # Takes in two dimensional array
    # as input and converts them
    # to a 1D array only. 
    # Do not use the builtin flatten function
    new_list = []

    return new_list

print(custom_flatten(seating_arrangement))
print(custom_flatten(random_numbers))


# Recursion

jumbled_list = [
    [1, 3, 4, ['a', 'b'], 5],
    [[[5], [2], [[100, ['LOL']], ['DOTA']]], [43]],
    [44, ['Covid 19', [['Extended', [30]]], 76, [4]], 90],
    [7, 8, 9, ['GGWP']]
]


def deep_flatten(lst):
    # Create a deep flatten function
    # that will flatten a list no matter how
    # deep the elements are.
    # The output should be a one dimensional list version
    # of the original list
    # HINT: You might need to use the type() function to check
    # if the item is list or not

    return

print(deep_flatten(jumbled_list))


def fibo(n):
    # Implement a recursive version of the 
    # nth fibonacci number.
    # Output should be a signle number
    # indicating the nth fibonacci number
    # NOTE: Create a trace similar to what we did in the class!

    return