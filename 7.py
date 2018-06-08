import numpy as np
import math
import utils.primes as primeUtil

def getXthPrime(x):
	primes = primeUtil.calculateFirstXPrimes(x, 10000)
	return primes[len(primes) - 1]

print getXthPrime(10001)


