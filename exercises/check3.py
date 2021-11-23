# Surname

# Lists
# Use the given list for the next 5 questions

num = [100, 200, 300, 400, 500, 600]

# Print the last element of the list 
# You cannot use num[len(num)-1] or num[5]
index_num = [ 5 ]
res_num = [num[i] for i in index_num] 
print(f'Question 1:')

print(res_num)

# Print the second to the fifth element of the list
index_num = [ 3 ]
res_num = [num[i] for i in index_num] 
print(f'Question 2:')

print(res_num)

# Add the item 700, 800 and 900 to the list to the list
num.append(700)
num.append(800)
num.append(900)
print(f'Question 3:')

print(num)

# Get the sum of all the numbers in num
# There is a function to get the sum of the list
total = sum(num) 
print(f'Question 4:')

print(f"Sum: {total}")

num += [100, 200, 300]
# Remove the duplicate in the list, then print it
# The data type should still be 'list'
num = set(num)

print(f'Question 5:')
print(f'{num}')

num = list(num)
print(type(num)) # This should still return 'list' as the data type

# For the next questions, refer to the list below
# This is a two dimentional list, this means that each element of the list
# is also a list.
# Perform the needed operation using this 2D list

#       blackboard
#
#  almeyda . . . . cuadra       ------- row 1
#  . . . . . . . . . . . .               . . 
#  pabilonia . . . . . . quinto ------- row 4

seating_arrangement = [
    ["almeyda", "avilledo", "bajar", "cuadra"],
    ["deguzman", "deocampo", "durana", "eclarin"],
    ["formanes", "mabilin", "mabunga", "oabel"],
    ["pajarillo", "pabilonia", "palines", "quinto"]
]

# print all the students seated on the second row.
print('Question 6:')
print(seating_arrangement[1])

# Add a new student "odasco" on the third row
print('Question 7:')
a_nested_list = seating_arrangement[2]
a_nested_list.append("odasco")
print(seating_arrangement)

# print the student seated at row 3 column 2
print('Question 8:')

print(seating_arrangement[2][1])

# print the seat mate of the student at row 1 column 4
print('Question 9:')

print(seating_arrangement[0][2])

# You might need to use a temporary variable for the next two questions
# swap the position of pabilonia and pajarillo
print('Question 10:')
temporary = [
    ["almeyda", "avilledo", "bajar", "cuadra"],
    ["deguzman", "deocampo", "durana", "eclarin"],
    ["formanes", "mabilin", "mabunga", "oabel"],
    ["pajarillo", "pabilonia", "palines", "quinto"]
]


temp = temporary[3][0]
temporary[3][0] = temporary [3][1]
temporary[3][1] = temp
print(temporary[3])

# swap the position of quinto and almeyda
print('Question 11:')
temp = temporary[0][0]
temporary[0][0] = temporary [3][3]
temporary[3][3] = temp
print(temporary)

# Add the students "rea", "rubio", "tabarina" and "zarsuelo"
# by creating another row.
print('Question 12:')
data = []
data = seating_arrangement
data.append(["rea", "rubio", "tabarina", "zarsuelo"])
#seating_arrangement = str(data) + str(seating_arrangement)
print(seating_arrangement)


# Use the given lists for the following questions
l1 = [6, 1, 22, 76, 23 , 90]
l2 = [9, 5, 31, 76, 12, 3]
l3 = [25, 11, 23, 98, 21, 5]

# combine all the list to a single list called l4
print('Question 13:')

l4 = l1 + l2 + l3  # change this
print(l4)

# print the maximum number in l4
# there is a function in list to find the biggest number
print('Question 14:')
print(max(l4))

# print the smallest number in l4
print('Question 15:')

print(min(l4))

# get all the numbers in l4 that are divisible by 3 and print them in a new list
# Use this as your reference: https://www.geeksforgeeks.org/filter-in-python/
print('Question 16:')

div_by_3 = list(filter(lambda x: x % 3 == 0, l4))   # change this
print(list(div_by_3))

"""
In 2-3 sentences, explain the method that you used and how it works
Write here:

I used the filter method wherein it filters a given sequence with the help of a function 
that tests each element in the sequence to be true or not and it is ussually used with Lambda functions to separate list, tuple, or sets. 
x % 3 == 0 shows that if an elements is divisible by 3, it will remain. 

"""


# Convert all items in l4 to string. All the elements should become string
# Return a new list that contains strings as elements.
# Refer to CODE 4 in this link https://www.geeksforgeeks.org/python-map-function/
# Remember how to convert variables!
print('Question 17:')

all_string = list(map(str, l4))    # change this
print(all_string)

"""
In 2-3 sentences, explain the method that you used and how it works
Write here:

I used the map function in which it returns a map object after making the elements of lists into a strings individually.
The code --->all_string = list(map(str, l4))<--- shows that the list from l4 was converted into a string.
"""