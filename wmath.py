# name comes from will math

import random
import conf

def atoi (x):
	if int(x):
		return int(x)
	else:
		return 0

def getrarity ():
	sum = 0
	for i in conf.rarities:
		sum += i[1]
	choice = int(random.random() * sum)
	for i in conf.rarities:
		if choice < i[1]:
			return i[0]
		else:
			choice -= i[1]
	# shouldn't get here if this works
	return conf.special_rarity

def stamp (size = conf.default_stamp_size):
	return ''.join(random.choice(conf.stamp_values) for i in range(size))
