import hashlib, time
import conf, wmath, wu

class Player:
	def __init__ (self):
		return None # TODO

class Token:
	cost = 0
	create_time = ""
	creator = ""
	hash = ""
	name = ""
	owner = ""
	seed = ""
	stamp = ""
	def __init__ (self, _creator = conf.anonymous, _name = conf.default_token_name, _tokens = None):
		# Token either needs to be created or loaded in. TODO
		# Assume that if no other tokens are passed, it is okay to mint a token
		self.new_token(_creator = _creator, _name = _name)

	def new_token (self, _creator = conf.anonymous, _name = conf.default_token_name):
		creator = _creator
		name = _name
		create_time = str(int(time.time()))
		stamp = wmath.stamp()
		seed = creator + ":" + name + ":" + create_time + ":" + stamp
		hash = hashlib.sha256(bytes(seed, conf.byte_encoding)).hexdigest()
		wu.log(conf.new_token_text % (seed, hash))

class Wallet:
	create_time = ""
	creator = ""
	hash = ""
	name = ""
	owner = ""
	seed = ""
	stamp = ""
	tokens = []
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
		owner = creator
		stamp = wmath.stamp()
		seed = creator + ":" + name + ":" + create_time + ":" + stamp
		hash = hashlib.sha256(bytes(seed, conf.byte_encoding)).hexdigest()
		wu.log(conf.new_wallet_text + seed, hash)
		self.tokens.append(Token())

class Cryptosystem:
	total_willcoin = 0
	bank = Wallet(_creator = conf.administration, _name = conf.bank_name)
	players = {}
	tokens = {} # The actual tokens, not just the hashes
	wallets = {} # The actual wallets, not just the hashes
	def __init__ (self, _location = None, _size = conf.default_cryptosystem_size):
		self.new_cryptosystem(_size)

	def new_cryptosystem (self, _size = conf.default_cryptosystem_size):
		total_willcoin = _size
