import numpy as np
import utils.primes as primeUtil

def sumOfPrimesBelow(number):
	primes = primeUtil.calculatePrimes(number)
	return np.sum(primes)

print sumOfPrimesBelow(2000000)


