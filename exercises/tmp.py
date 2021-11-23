# DE Torres

# Create the following shapes using the variable "cnt"
# In each shape, please take note of the minimum
# and maximum value of cnt. Your code should work on all these cases.

# Always check for the possible min and max value
# min <= cnt <= max

# use only TWO while loop for each item
# Some items require you to take a picture of the paper tracing for values i and j

cnt = 10

print("Shape 1 - 3 <= cnt <= 30")
# Also take a picture of the paper tracing of variables i and j

# 
#
# * * * * *
# * * * *
# * * *
# * *
# *
i = 0 # first loop
j = 0 # second loop
while i < cnt:
  while j <= cnt:
    if j < cnt - i:
      print("*", end = "") # print *
    else:
      print("", end = "")  # print spaces
    j += 1    # increment of second lop

  print("")   # new line
  j = 0     # reset j to 0
  i += 1      # increment of first loop

print("Shape 2 - 5 <= cnt <= 30")

# 
#
# * * * * *
# * *     *
# *   *   *
# *     * *
# * * * * *

i = 0 # first loop
j = 0 # second loop
while i < cnt:
  while j < cnt:
    if i == 0 or i == (cnt - 1) or j == 0 or j == (cnt-1) or i == j: # all the codition to print *
      print("*", end = " ") # print *
    else:
      print(" ", end = " ")  # print spaces
    j += 1    # increment of second lop

  print("")   # new line
  j = 0     # reset j to 0
  i += 1      # increment of first loop

print("Shape 3, 1 <= cnt <= 30")
# Also take a picture of the paper tracing of variables i and j
# 
#
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# 
#
# *

# 
# * *
# * *


i = 0 # first loop
j = 0 # second loop
while i < cnt:
  if cnt > 30: # to have 30 as maximum
    break
  while j < cnt:
    if i == 0 or i == (cnt - 1) or j == 0 or j == (cnt-1): # all the codition to print *
      print("*", end = " ") # print *
    else:
      print(" ", end = " ")  # print spaces
    j += 1    # increment of second lop

  print("")   # new line
  j = 0     # reset j to 0
  i += 1      # increment of first loop

print("Shape 4, 3 <= cnt <= 30")
# Hint, there might be two different filters for odd or even number


# 
# *   *
#  * *
#   *
#  * *
# *   *

# 
# *   *
#  * *
#  * *
# *   *
i = 0 # first loop
j = 0 # second loop
while i < cnt:
  if cnt > 30 or cnt < 3: # to have 30 as maximum and 3 as minimum
    break
  while j < cnt:
    if i == j or j == (cnt-i-1): # all the codition to print *
      print("*", end = " ") # print *
    else:
      print(" ", end = " ")  # print spaces
    j += 1    # increment of second lop

  print("")   # new line
  j = 0     # reset j to 0
  i += 1      # increment of first loop


print("Shape 5, 3 <= cnt <= 30")
# Also take a picture of the paper tracing of variables i and j

# 
#
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


i = 0 # for the first loop
j = 0 # for the second loop

#first loop
while i < cnt:
  # second loop
  while  j < cnt :
    if j < i:               # condition to print space
      print(" ", end=" ")
    else:
      print("*", end =" ") # prints *
    j += 1
  
  print("") # creates new line
  #Resets the j variable
  j = 0
  i += 1

print("Shape 6, 4 <= cnt <= 30")


# 

# * * * * *
#   *
#     *
#       *
# * * * * *

# 
# * * * *
#   *
#     *
# * * * *

i = 0 # first loop
j = 0 # second loop
while i < cnt:
  if cnt > 30 or cnt < 4: # to have 4 and 30 as minimum and maximum
    break
  while j < cnt:
    if i == 0 or i == (cnt - 1) or i == j: # all the codition to print *
      print("*", end = " ") # print *
    else:
      print(" ", end = " ")  # print spaces
    j += 1    # increment of second lop

  print("")   # new line
  j = 0     # reset j to 0
  i += 1      # increment of first loop

print("Shape 7, 3 <= cnt <= 30")


# 
#
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

i = 0
j = 0
#first loop
while i < (2 * cnt -1):
  # second loop
  if cnt < 3 or cnt > 30:
    break
  while  j < cnt :
    if j < (((2 * cnt-i)-2) if i >= cnt else i):
              # condition to print space
      print(" ", end=" ")
    else: 
      print("*", end =" ")    # prints *
    j += 1
  
  print("") # creates new line
  #Resets the j variable
  j = 0
  i += 1

print("Shape 8, 3 <= cnt <= 30")
# Also take a picture of the paper tracing of variables i and j

# 
#
# * * * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

i = 0 # for the first loop
j = 0 # for the second loop

while i < (2 *cnt-1):
  if cnt < 3 or cnt > 30: # to have maximum and minimum
    break
  while j < cnt:
    if j < ((i - cnt +2)  if i >= cnt else cnt - i):  # conditions to print *
      print("*", end = " ") # print *
    else:
      print("", end = " ")   # print spaces
    j += 1    # increment of second loop

  print("")   # new line
  j = 0     # reset j to 0
  i += 1      # increment of first loop

print("Shape 9, 3 <= cnt <= 30")


# 

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

i = 0
j = 0

while i < cnt:
  if cnt < 3 or cnt > 30:
    break
  while j <= cnt:
    if j < cnt - i:       #print spaces
      print(" ", end = "")
    else:
      print("*", end = " ")
    j += 1    # increment of second loop

  print("")   # new line
  j = 0     # reset j to 0
  i += 1      # increment of first loop
#first loop
print("Shape 10, 3 <= cnt <= 30")


# 

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

i = 0 # for the first loop
j = 0 # for the second loop

#first loop
while i < cnt:
  # second loop
  while  j < cnt :
    if j < i:               # condition to print space
      print(" ", end="")
    else:
      print("*", end =" ") # prints *
    j += 1
  
  print("") # creates new line
  #Resets the j variable
  j = 0
  i += 1

print("Shape 11, 3 <= cnt <= 30")

# 
#   *
#  * *
# * * *
#  * *
#  * *

# 
#    *
#   * *
#  * * *
# * * * *
#  * * * 
#  * * *
#  * * *

# 
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#  * * * *
#  * * * *
#  * * * *

i = 0
j = 0

while i < 2*cnt-1:
  if cnt < 3 or cnt > 30:
    break
  while j <= cnt:
    if j < cnt - i: #print spaces
      print(" ", end = "")
    elif j == (0 if i>=cnt else "none"):
      print(" ", end = " ")
    elif j == (cnt if i>=cnt else "none"):
      print(" ", end = " ")
    else:
      print("*", end = " ")
    j += 1    # increment of second loop
  print("")   # new line
  j = 0     # reset j to 0
  i += 1      # increment of first loop

print("Shape 11, 3 <= cnt <= 30")

# 

# *
# * *
# * * *
# * *
# *


# 

# *
# * * 
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
i = 0
j = 0
#first loop
while i < (2 * cnt -1):
  # second loop
  if cnt < 3 or cnt > 30:  # minimum and maximum
    break
  while  j <= cnt :
    if j < ((2 * cnt-i -1) if i >= cnt else i + 1):
              # condition to print space
      print("*", end=" ")
    else: 
      print(" ", end =" ")    # prints *
    j += 1
  
  print("") # creates new line
  #Resets the j variable
  j = 0
  i += 1

print("Shape 12, 3 <= cnt <= 30")


# 
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
# * * * * *

for i in range (1,cnt + 1):       
    if cnt < 3 or cnt > 30:
      break
    # Print trailing spaces 
    for j in range (1,cnt - i + 1): 
        print (end=" ")
              
  # Print stars after spaces 
          
    for j in range (1,cnt + 1): 
        print ("*",end="") 
              
    # Move to the next line/row 
    print()

print("Shape 13, 3 <= cnt <= 30")


# 

# * * * * *
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *

for i in range (1, cnt + 1):
  if cnt < 3 or cnt > 30:
    break
  #print trailing spaces
  for j in range(1,i):
    print(end =" ")
  # print * after the spaces
  for j in range(1, cnt + 1):
    print("*",end="")
  #next row
  print("")

print("Shape 14, 3 <= cnt <= 30")

# 
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
# * * * * *
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *

for i in range (1,2*cnt):       
    if cnt < 3 or cnt > 30: # minimum and maximum
      break
    # Print trailing spaces 
    if i < cnt:                   # for the first half
      for j in range (1,cnt - i + 1): 
          print (end=" ")
    else:                         # for the next half
      for j in range(1, i-cnt+1):
        print (end=" ")
    for j in range (1,cnt + 1): 
        print ("*",end="") 
              
    # Move to the next line/row 
    print()
