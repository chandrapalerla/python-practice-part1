numbers = []
for x in range(5):
    numbers.append(x)
print(numbers)

numbers1 = [x * x for x in range(10) if x % 2 == 0]
print(numbers1)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
print(combs)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = []
for row in matrix:
    for num in row:
        flat.append((num))

print(flat)

flat1 = [num for row in matrix for num in row]
print(flat1)