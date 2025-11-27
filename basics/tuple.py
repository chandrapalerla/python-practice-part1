#creating tuples
t1 = () #empty tuple

t2 = (1,2,3) #tuple with 3 elements

t3 = (1,"hello",3.4,True) #tuple can have different data types

t4 = (2,[4.5],(5,6)) #Nested tuple

print(t4)

t5 = 1,2,3,3,4,5 #tuple packing
print(t5)

a,b,c = (20,30,40) #tuple unpacking
print(a,b,c)
#accessing tuple elements
print(t5[0]) #indexing
print(t5[:2]) #slicing
print(t5[-1]) #negative indexing
print(len(t5)) #length of tuple

#Tupe methods
print(t5.index(5)) #returns index of first occurence of value
print(t5.count (3)) #returns count of value in tuple

#built-in functions with tuple
print(max(t5)) #maximum value in tuple
print(min(t5)) #minimum value in tuple
print(sum(t5)) #sum of all elements in tuple
print(sorted(t5)) #returns sorted list of tuple elements
print(tuple(sorted(t5))) #returns sorted tuple


#Real use case of tuples
# Database row (fixed structure)
employee = ("E123", "Alice", "HR", 55000)

# Accessing fields (like sequences)
print(employee[1])  # Alice
print(employee[-1]) # 55000

# Iterating over employee data
for field in employee:
    print(field)
