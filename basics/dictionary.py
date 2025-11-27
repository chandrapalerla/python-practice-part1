# Creating and manipulating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Creating dictionary using dict()
person2 = dict(name="chandu", age=34, city="hyd")
print(person2)

# Creating dictionary from list of tuples
person3 = dict([("name", "komali"), ("age", 9), ("city", "hyd")])
print(person3)

# creating dictionary using fromkeys()
keys = ['name', 'age', 'city']
default_value = 'unknown'
person4 = dict.fromkeys(keys, default_value)
print(person4)  # {'name': 'unknown', 'age': 'unknown', '

# creating dictionary using zip()
keys = ['name', 'age', 'city']
values = ['Bob', 25, 'Los Angeles']
person5 = dict(zip(keys, values))
print(person5)  # {'name': 'Bob', 'age': 25, '

# creating nested dictionary
people = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(people)

# Accessing dictionary elements
print(person["name"])  # Alice
print(person.get("age"))  # 30
print(person.get("country", "USA"))  # USA (default value)

for key, values in person.items():
    print(key, ":", values)


for per1 in people.values():
    print(per1)