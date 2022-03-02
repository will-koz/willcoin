import hashlib, time
import conf, wmath

class Wallet:
	creator = ""
	hash = ""
	name = ""
	seed = ""
	stamp = ""
	create_time = ""
	def __init__ (self,
		_creator = conf.anonymous, _name = conf.default_wallet_name, _players = None):
		if _players == None:
			# if no players are passed, it is okay to assume that the wallet is okay to make
			self.new_wallet(_creator = _creator, _name = _name, _players = _players)

	def new_wallet (self,
		_creator = conf.anonymous, _name = conf.default_wallet_name, _players = None):
		creator = _creator
		name = _name
		create_time = str(int(time.time()))
		stamp = wmath.stamp()
		seed = creator + ":" + name + ":" + create_time + ":" + stamp
		hash = hashlib.sha256(bytes(seed, conf.byte_encoding)).hexdigest()
		print(seed)
		print(hash)

class Cryptosystem:
	total_willcoin = 0
	bank = Wallet(_creator = conf.administration, _name = conf.bank_name)
	def __init__ (self, _location = None, _size = conf.default_cryptosystem_size):
		self.new_cryptosystem(_size)

	def new_cryptosystem (self, _size = conf.default_cryptosystem_size):
		total_willcoin = _size
