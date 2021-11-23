# loops

letter = ["a", "b", "c", "d", "e", "f"]
i = 0 # counters

# while(i < len(letter)):
#     print(f"Letter is: {letter[i]}")
#     i += 1

nums = [54, 22, 95, 1234, 4, 87, 1, 26, 100]
j = 0 # counters

while(j < len(nums)):
    # use if else

    if nums[j] % 2 == 0 and nums[j] % 5 == 0:
        print(nums[j])    

    j += 1 # increment counter


k = 0

while(True):
    if k == 345:
        print("Found 345!!!!")
        break       # Stop the loop

    k += 1


nums = []
# For loops automatically stop
for x in nums:
    print(x)


