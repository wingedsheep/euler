import numpy as np
import math

def largestPalindromeOfProduct(digits):
	lowest = int(math.pow(10, digits - 1))
	highest = int(math.pow(10, digits))

	highestPalindrome = 0
	for i in range(lowest, highest):
		for j in range(i, highest):
			product = i * j
			if product > highestPalindrome:
				if isPalindrome(product):
					highestPalindrome = product
	return highestPalindrome

def isPalindrome(number):
	text = str(number)
	if text == text[::-1]:
		return True

print largestPalindromeOfProduct(3)