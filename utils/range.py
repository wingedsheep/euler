import numpy as np

def reverseRange(*args):
	highest = args[0]
	lowest = args[1]
	if len(args) > 2:
		step = args[2]
	else:
		step = 1

	return range(highest, lowest, -step)