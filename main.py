from binoxxo import Binoxxo
import time
import random

size = 10

b = Binoxxo(size)
b = b.set(0,0,'x')
b = b.set(0,1,'x')
b = b.set(0,2,'o')

start = time.time()

n = 0


def backtracking_generator(binoxxo):
	global n
	n += 1
	if binoxxo.is_complete():
		print("{} steps".format(n))
		print(binoxxo)
		return True
	for b in binoxxo.get_possible_next_moves():
		if not b.is_viable():
			return False
		if backtracking_generator(b):
			return True
	return False


backtracking_generator(b)
print(str(time.time() - start) + "seconds")
