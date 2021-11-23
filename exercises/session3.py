hobbies = ["music", "frisbee", "dota", "cooking", "sleeping"]

# accessing element of a list
print(hobbies[0])

# getting legnth of a list
print(len(hobbies))

l = len(hobbies)
# Get last element
print(hobbies[l - 1])

# Chaging values
hobbies[1] = "PUBG"
print(hobbies)

hobbies.append("swimming")
print(hobbies)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

# This prints a range from index x, to index y-1 x:y
print(nums[1:5])
print(nums[1:])

# This prints the element of the list
# for n in nums:
#     for n1 in nums:
#         print(n * n1, end = ' ')
#     print("")

tuple_num = tuple(nums)
print(tuple_num)

set_num = set(nums)
print(set_num)

# Dictionary

my_car = {
    "brand": "subaru",
    "model": "xv",
    "year_released": 2018,
    "available_colors": ["red", "white", "orange"],
    "is_electric": True,
    "engine_size": 1.8
}

# Accessing elements
print(f"Car brand {my_car['brand']}, model: {my_car['model']}")
print(my_car.get("brand"))

my_car.get("brand") == my_car["brand"]

# Assigning new values
my_car["year_released"] = 2019
print(my_car["year_released"])



my_car = {
    "brand": "subaru",
    "model": "xv",
    "year_released": 2018,
    "available_colors": ["red", "white", "orange"],
    "is_electric": True,
    "engine_size": 1.8
}


# print the legnth of available colors
l = len(my_car["available_colors"])
print(f"Colors: {l}")

# Add another key called "interior" and set the value to "leather"
my_car["interior"] = "leather"
print(my_car)
