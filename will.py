import hashlib, time
import conf, wmath

class Wallet:
	creator = ""
	hash = ""
	name = ""
	seed = ""
	def __init__ (self, creator = conf.anonymous, name = conf.default_wallet_name, players = None):
		seed_prefix = creator + "-" + name + ":"
		seed_suffix = str(int(time.time())) + "-" + wmath.stamp()
		if players == None:
			# if players are not passed, assume that it is okay to make a new wallet
			hash = hashlib.sha256(bytes(seed_prefix + seed_suffix, conf.byte_encoding)).hexdigest()
			print(seed_prefix + seed_suffix)
			print(hash)

class Cryptosystem:
	total_willcoin = 0
	bank = Wallet(creator = conf.administration, name = conf.bank_name)
	def __init__ (self, location = None, size = conf.default_cryptosystem_size):
		self.new_cryptosystem(size)

	def new_cryptosystem (self, size = conf.default_cryptosystem_size):
		total_willcoin = size
