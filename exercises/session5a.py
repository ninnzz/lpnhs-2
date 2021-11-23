# Control flow examples
import random

count = 5
i = 0

while i < count:
    print("*", i)
    i += 1

num = [1, 2, 3, 4, 5]

for x in num:
    print(x ** 2)

i = 0
while i < len(num):
    print("Value of i", i)
    print(num[i])

    i += 1

# Function
def is_div_by(n, d):
    return n % d == 0

# Use l1 for the following questions
# creates a list of 50 random number
l1 = random.sample(range(-100, 100), 50)


i = 0
# Print all the numbers divisible by 5 and 2
while i < len(l1):
    if is_div_by(l1[i], 5):
        print(l1[i])

    i += 1

for x in l1:
    if is_div_by(x, 5):
        print(x)

l2 = list(range(1, 11))

for y in l2:
    for x in l2:
        print(x * y, end = ' ')
    print('')


i = 0
j = 0
while i < len(l2):
    while j < len(l2):
        p = l2[j] * l2[i]
        if is_div_by(p, 2):
            print(p, end=" ")
        else:
            print("X", end=" ")
        j += 1
    print("")
    j = 0
    i += 1


cnt = 5

i = 0
j = 0

while i < cnt:
    while j <= cnt:
        print("* ", end="")
        j += 1      # increment of second loop

    print("")       # new line
    j = 0           # reset j to 0
    i += 1          # increment of first loop

#         *
#       * *
#     * * *
#   * * * *
# * * * * *







