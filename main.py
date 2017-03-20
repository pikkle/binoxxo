from binoxxo import Binoxxo
import time

size = 8

b = Binoxxo(size)
start = time.time()

n = 0
def backtracking_generator(binoxxo):
	global n
	n += 1
	print(binoxxo)
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
