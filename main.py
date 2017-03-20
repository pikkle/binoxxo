from binoxxo import Binoxxo
import time

size = 10

b = Binoxxo(size)
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
		if b.is_viable() and backtracking_generator(b):
			return True
	return False


backtracking_generator(b)
print(str(time.time()-start) + "seconds")