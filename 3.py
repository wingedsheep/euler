import numpy as np
from utils.primes import isPrime

def largestPrimeFactor(number):
	i = 2
	while i < number / 2:
		divided = number / i
		if isFactor(number, divided) and isPrime(divided):
			return divided
		i += 1

def isFactor(number, factor):
	return number % factor == 0

print largestPrimeFactor(600851475143)