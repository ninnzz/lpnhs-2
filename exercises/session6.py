# Functions
import random
# def hello(name, age):
#     print(f"Hello {name}")

# hello("Garci", 1)

l1 = random.sample(range(0, 100), 80)
l2 = random.sample(range(0, 100), 80)
l3 = random.sample(range(0, 100), 80)

l4 = l1 + l2 + l3

# Linear search
def search(n, lst):
    """
    Search for number n on lst
    """
    for i in lst:
        if i == n:
            return True
    return False

def search_count(n, lst):
    """
    Search for "n" and count the number of occurances
    """
    count = 0

    for i in lst:
        if i == n:
            count += 1
    
    return count

# Asks input in command line
user_input = int(input("Enter a number [0-100]:"))

count = search_count(user_input, l4)

print(f"The number of {user_input} in list is {count}")

