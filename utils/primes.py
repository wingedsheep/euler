import numpy as np
import math

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

def calculatePrimesForRange(alreadyFoundPrimes, uncheckedMin, uncheckedMax):
	primes = alreadyFoundPrimes

	if uncheckedMin % 2 == 0:
		if uncheckedMin == 2:
			primes = np.concatenate((np.array([2], dtype = 'int'), np.arange(uncheckedMin + 1, uncheckedMax + 1, 2, dtype = 'int')))
		else:
			primes = np.concatenate((np.array(primes, dtype = 'int'), np.arange(uncheckedMin + 1, uncheckedMax + 1, 2, dtype = 'int')))
	else:
		primes = np.concatenate((np.array(primes, dtype = 'int'), np.arange(uncheckedMin, uncheckedMax + 1, 2, dtype = 'int')))

	currentIndex = len(alreadyFoundPrimes)

	if len(alreadyFoundPrimes) > 1:
		for i, p in enumerate(alreadyFoundPrimes[1:]):
			if p >= math.sqrt(uncheckedMax):
				break
			primes = __filterMultiples(primes, currentIndex, p)

	while currentIndex < len(primes) and primes[currentIndex] < math.sqrt(uncheckedMax):
		current = primes[currentIndex]
		primes = __filterMultiples(primes, currentIndex + 1, current)
		currentIndex += 1

	return primes

def calculatePrimes(max):
	return calculatePrimesForRange([], 2, max)

def calculateFirstXPrimes(x, stepSize = 1000):
	foundPrimes = []
	currentNumber = 2
	while len(foundPrimes) < x:
		foundPrimes = calculatePrimesForRange(foundPrimes, currentNumber, currentNumber + stepSize)
		currentNumber += (stepSize + 1)

	return foundPrimes[0:x]

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