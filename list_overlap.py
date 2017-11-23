import random

def list_overlap():

	a = random.sample(range(10), 3)
	b = random.sample(range(10), 3)
	for i in a:
		if i in b:
			print(i)

list_overlap()