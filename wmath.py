# name comes from will math

import random
import conf

def stamp (size = conf.default_stamp_size):
	return ''.join(random.choice(conf.stamp_values) for i in range(size))

def getrarity ():
	sum = 0
	for i in conf.rarities:
		sum += i[1]
	choice = random.
	for i in conf.rarities:
