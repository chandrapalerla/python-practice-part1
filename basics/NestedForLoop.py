numbers = [8,7,2,5,3,1]
target = 10

for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j] == target:
            print('Pair found:', numbers[i], numbers[j])

