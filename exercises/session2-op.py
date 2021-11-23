# operators
x = 1
y = 2
z = 3

# AR operations
add = x + y
sub = z - y
mult = z * x
div = z / x


new_val = ((x + y) * (z / 1)) * 4
print(new_val)


print(f"add: {add}, sub: {sub}, mult: {mult}, div: {div}")
# Checks the type of the specific variable
print(type(div))

# Assignment operations
x += 1
# print(x)

# Comparison operation
# print(x == 2) # Will return true
# print(x == y) # Will return true
# print(x != y) # Will return False
# print(x < y) # Will return false
# print(x <= y) # Will return true
c = (x == 2)
# print(c)

# Logical Operators
f1 = (x == 2) and (x == y) # True true
print(f1)

f2 = (x != 2) or (x != y) # true false
print(f2)

f3 = not f1
print(f3)

f4 = x is 2
print(f4)

f5 = x is not z
print(f5)





