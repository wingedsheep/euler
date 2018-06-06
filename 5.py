import numpy as np
import math

def evenlyDivisibleByNumbersUntil(number):
	# We can filter out the bottom half of the numbers that should be divisible, since the higher the number the more restrictive it is.
	# For example if a number should be divisible by 10, we can filter out 5, 2 and 1, because if a number is divisible by 10, it is also divisible by 5, 2 and 1.
	# For 8 we can filter out 4, 2 and 1.
	# For 6 we can filter out 3, 2 and 1.
	# So for the range 1..10 we are then left with 6..10 since 1..5 can be filtered out.
	minimum = int(math.ceil(number / 2))
	shouldBeDivisibleBy = list(range(minimum, number + 1))

	# We start by checking the minimum number * 2, since the outcome should always be a multiple of the minimum, but can't be lower than the maximum number in the divisible by list.
	i = minimum * 2
	while True:
		divisibleByAll = True
		for value in shouldBeDivisibleBy:
			if i % value != 0:
				divisibleByAll = False
				break
		if divisibleByAll == True:
			return i
		# Since the number should always be divisible by the minimum number left in the set, there is no use in adding anything less than this number to the current for each step.
		i += minimum

print evenlyDivisibleByNumbersUntil(20)