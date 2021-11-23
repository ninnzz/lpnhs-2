# exer

a = 10
i = 0 # for the first loop
j = 0 # for the second loop

# first loop
while i < a:
    # second loop
    while j <= i:
        print("*", end=" ")
        j += 1
    
    print("")
    j = 0 # Resets the j variable
    i += 1

# i and j tracking of values

# i - j
# 0   0
# 0   1
# 1   0
# 1   1
# 1   2
# 2   0
# 2   1
# 2   2
# 2   3
# 3   0
# 3   1
# 3   2
# 3   3
# 3   4
# 4   0
# 4   1
# 4   2
# 4   3
# 4   4
# 4   5
# 5   0 <--- ended here because i < 5