s = {1, 2, 3, 4, 2}
print(s)

s.add(6)
print(s)

s.remove(2)
print(s)

baskets = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for basket in baskets:
    if basket == "apple":
        print(basket)
    break
print("apple" in baskets)

print(len(baskets))

