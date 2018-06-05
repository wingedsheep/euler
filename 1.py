sumOfMultiples = 0

for i in range(1, 1000):
    if (i % 5 == 0):
        sumOfMultiples += i
    elif (i % 3 == 0):
        sumOfMultiples += i

print sumOfMultiples