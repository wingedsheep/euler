import numpy as np
import math

def pythagoreanTriplet(sum):
	for c in range(1,sum):
		for b in range (c - 1, 0, -1):
			a = sum - c - b
			if a >= b:
				break
			if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
				return (a, b, c)

print np.product(pythagoreanTriplet(1000))


