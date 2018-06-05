import numpy as np

def __isPrime(number, prevPrimes, currentIndex):
	for prime in prevPrimes[1:currentIndex - 1]:
		if number % prime == 0:
			return False
	return True

def __filterMultiples(primes, startingIndex, currentNr):
	currentIndex = startingIndex
	indicesToRemove = []
	while currentIndex < len(primes):
		if primes[currentIndex] % currentNr == 0:
			indicesToRemove.append(currentIndex)
		currentIndex += 1
	return np.delete(primes, indicesToRemove)

def calculatePrimes(max):
	primes = np.arange(1, max + 1)

	currentIndex = 1
	prevLenPrimes = len(primes)
	while currentIndex < len(primes):
		current = primes[currentIndex]
		primes = filterMultiples(primes, currentIndex + 1, current)

		if (prevLenPrimes == len(primes)):
			break

		prevLenPrimes = len(primes)

		currentIndex += 1
	return primes

def isPrime(number):
	i = 2
	while i < number / 2:
		if number % i == 0:
			return False
		if i == 2:
			i += 1
		else:
			i += 2
	return True