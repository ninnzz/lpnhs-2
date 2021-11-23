# bubble_sort.py
import random

# [4, 8, 2, 1]  j = 3, i = 0
# [4, 2, 8, 1]  j = 3, i = 1
# [4, 2, 1, 8]  j = 3, i = 2
# [2, 4, 1, 8]  j = 2, i = 0
# [2, 1, 4, 8]  j = 2, i = 1
# [1, 2, 4, 8]  j = 1, i = 0

def bubble_sort(lst):
    for j in range(len(lst)-1 ,0 , -1):
        for i in range(j):
            if lst[i]['rank'] > lst[i+1]['rank']:       # Compares the element
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp

    return lst


# unsorted = random.sample(range(1, 20), 10)
# print(unsorted)
# print(bubble_sort(unsorted))

list_dict = [{'rank': 2}, {'rank': 1}, {'rank': 10}, {'rank': 8}]
print(bubble_sort(list_dict))