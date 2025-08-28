for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# Pass in function

def my_func():
    pass


print("Function defined successfully")

for i in range(5):
    if i == 2:
        pass  # just placeholder, nothing happens
    elif i == 3:
        continue  # skip printing 3
    elif i == 4:
        break  # exit loop
    print(i)
