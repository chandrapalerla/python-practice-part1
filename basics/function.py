def fib(num):
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a + b
        print()


fib(200)


# Function with Return Value
def add(a, b):
    return a + b


result = add(10, 20)
print(f"result = {result}")


# Default Argument Values

def greet(name="chadu"):
    print(f"Hello {name}")


greet()


# Keyword Arguments

def argument(name, age):
    print(f"my name is :{name} , age is {age}")

argument(age=34, name="chandu")


def greeting(name,/,message = "Hello"):
    print(f"{message},{name}|")

greeting("chandu")
greeting("chandu",message="hi")

def order(item, *, quantity=1, price=0):
    print(f"Item: {item}, Quantity: {quantity}, Price: {price}")

order("Book", quantity=3, price=100)   # ✅ correct
#order("Book", 3, 100)

#Lambda Functions

addition = lambda x: x + 10
print(addition(5))

def outer():
    def inner():
        print("This is the inner function")
    inner()

outer()