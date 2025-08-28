fruits = ["apple", "banana", "cherry"]
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

#basic operations
print(fruits[0])  # Accessing elements
print(fruits[-2])  # Negative indexing
print(fruits[1:3])  # Slicing
print(len(fruits))  # Length of the list

#changing elements
fruits[1] = "blueberry"
print(fruits)

#Removing elements
fruits.remove("blueberry")   # remove by value
fruits.pop(1)            # remove by index
del fruits[0]            # delete element
print(fruits)

#Adding elements
fruits.append("date")
print(fruits)

#Adding specific position
fruits.insert(1, "banana")
print(fruits)

#List Functions and Methods
print(len(nums))        # 4
print(max(nums))        # 40
print(min(nums))        # 10
print(sum(nums))        # 100

nums.reverse()  # reverses list
print(nums)
nums.sort()             # ascending sort
print(nums)
nums.sort(reverse=True) # descending sort
print(nums)

#Iterating through a list
for fruit in fruits:
    print(fruit)

#Iterate with index
for index, fruit in enumerate(fruits):
    print(index, fruit)

    # Normal way
    squares = []
    for i in range(5):
        squares.append(i ** 2)

    # List comprehension
    squares = [i ** 2 for i in range(5)]
    print(squares)  # [0, 1, 4, 9, 16]

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

print("date" in fruits)   # True
print("grape" not in fruits)  # True

words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # ['apple', 'banana', 'cherry']

#Zipping lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)

# Creating list
list1 = []
list2 = list()
list3 = list(range(5))
list4 = [x * x for x in range(10)]

print(list1)
print(list2)
print(list3)
print(list4)

# Indexing and slicing
print(list4[3])
print(list4[:4])

# Add or remove
list4.append(500)  #
list4.extend([501, 502])
print(list4)

list4.reverse()
print(list4)

list5 = [2, 3, 4, 1, 3, 5, 9, 7, 6]
list5.sort()
print(list5)

list6 = ["chandu", "kaushik", "komali"]
list6.sort(key=len)
print(list6)

#Using List As Stacks
stack= [3,4,5]
stack.append(6)
print(stack)
stack.pop()
print(stack)
