from binoxxo import Binoxxo
from random import randint, getrandbits
import time

size = 10

start = time.time()
tries = 0

def print_stats():
	t = time.time()-start
	print("%.2f tries/s, %d tries total, %.2f seconds" % (tries / t, tries, t), end="\r")

while True:
	binoxxo = Binoxxo(size)
	tries += 1
	if (tries % 100 == 0 or tries == 10):
		print_stats()
	count = 1
	empty_spots = []
	empty_spots_counter = 0
	while not binoxxo.is_complete():
		tmp = binoxxo.get_empty_spots()
		if (tmp != empty_spots):
			empty_spots = tmp
			empty_spots_counter = 0
			r = randint(0, len(empty_spots)-1)
			(x, y) = empty_spots[r]
		else:
			if (empty_spots_counter >= len(empty_spots)):
				break
			else:
				(x, y) = empty_spots[empty_spots_counter]
				empty_spots_counter += 1
		val = 'x' if (getrandbits(1)) else 'o'
		try:
			binoxxo.set(x, y, val)
		except:
			continue
		count += 1

	if (binoxxo.is_complete()):
		print("HOORAAAAY")
		print(binoxxo)
		break