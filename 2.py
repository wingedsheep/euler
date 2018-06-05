evenFibonnaciSum = 0

prev = 1
current = 2
while current < 4000000:
	if (current % 2 == 0): 
		evenFibonnaciSum += current
	new = prev + current
	prev = current
	current = new  

print evenFibonnaciSum