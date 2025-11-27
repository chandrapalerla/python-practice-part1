name = 'chandu'
print(name)
length = len(name)
print(length)
# Convert string to list for in-place reversal
name_list = list(name)
left = 0
right = length - 1
while left < right:
    temp = name_list[left]
    name_list[left] = name_list[right]
    name_list[right] = temp
    left += 1
    right -= 1
# Join the list back to a string
reversed_name = ''.join(name_list)
print(reversed_name)
