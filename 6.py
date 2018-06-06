import numpy as np
import math

def sumOfSquares(number):
	# For the sum of squares we have an addition at every step. But there is also an addition to the addition that increases by 2 every step.
	# Example:
	# number = 1; result = 1; addition = 1;
	# number = 2; result = 5; addition = 4; additionToAddition = 3;
	# number = 3; result = 14; addition = 9; additionToAddition = 5;
	# number = 4; result = 30; addition = 16; additionToAddition = 7;
	# number = 5; result = 55; addition = 25; additionToAddition = 9;
	# So we see there is a linear increase in the addition to the addition
	addition = 1
	additionToAddition = 3

	total = 0

	i = 1
	while i <= number:
		total += addition
		addition += additionToAddition
		additionToAddition += 2
		i += 1

	return total

def sum(number):
	# The sum for a range of natural numbers increases with a step size (i) that increases by 1 every step
	# example:
	# number = 1; sum = 1;
	# number = 2; sum = 3; // Step of 2
	# number = 3; sum = 6; // Step of 3
	# number = 4; sum = 10; // Step of 4
	i = 1
	sum = 0
	while i <= number:
		sum += i
		i += 1

	return sum

def squareOfSum(number):
	return int(math.pow(sum(number), 2))

def differenceBetweenSumOfSquaresAndSquareOfSum(number):
	return squareOfSum(number) - sumOfSquares(number)

print differenceBetweenSumOfSquaresAndSquareOfSum(100)