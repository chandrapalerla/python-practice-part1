#iterating list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#iterating string
str = 'chandrasheakr'
for char in str:
    print(char)

#iterating range
for i in range(5):
    print(i)

for i in range(1,6,2):
    print(i)

# using else with for loop
for i in range(5):
    print(i)
    if(i == 3):
        print("Breaking the loop at i =", i)
        break
else:
    print("Loop completed successfully.")

# using break and continue
for name in ["chandu","kaushik","komali"]:
    if name == "kaushik":
        print("Skipping kaushik")
        continue
    print(name)

# Iterating with enumerate(index+value)
colors = ['red', 'green', 'blue']
for index,color in enumerate(colors):
    print(index,color)

# Looping over a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in my_dict.items():
    print(f"{key}: {value}")

for key in my_dict:
    print(key)
for valu in my_dict.values():
    print(valu)