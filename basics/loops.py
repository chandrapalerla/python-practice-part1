i = 0
while i < 5:
    print(i)
    i += 1

min_length = 2
name = input("enter the name: ")
while not (len(name) >= min_length and name.isalpha() and name.isprintable()):
    name = input("enter the name: ")
print(f"Hello {name}")

l = [1, 2, 3, 10]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)
    print(l)


a = 10
b = 0
try:
    a/b
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
finally:
    print("This will always execute, regardless of an error.")



