x = 4
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("something else")

# match Multiple Values
day = "Monday"
match day:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Monday":
        print("It's Monday, back to work.")
    case _:
        print("It's a weekday.")

# match with Guard Conditions
num = 15
match num:
    case x if x < 0:
        print("Negative number")
    case x if x == 0:
        print("Zero")
    case x if x > 0:
        print("Positive number")


# match with Data Structures
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, 0):
        print(f"X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# match with Class Instances
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)

match p:
    case Person(name="Alice", age=30):
        print("This is Alice, age 30")
    case Person(name=name, age=age):
        print(f"Person {name}, age {age}")
