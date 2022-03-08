import time
import conf, wmath, wu

class Player:
	name = ""
	wallets = []
	def __init__ (self, _name = None, _wallets = None):
		# Like many other classes, can be loaded in or created TODO
		self.new_player(_name = _name, _wallets = _wallets)

	def new_player (self, _name = None, _wallets = None):
		# TODO Throw an error. _name should never be None.
		name = _name
		wallets = _wallets

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
		hash = wu.whash(seed)
		wu.log(conf.text_new_token % (seed, hash))

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
		# if no object is passed, it is okay to assume that the wallet is okay to make TODO
		self.new_wallet(_creator = _creator, _name = _name, _players = _players)

	def new_wallet (self,
		_creator = conf.anonymous, _name = conf.default_wallet_name, _players = None):
		# TODO make sure that this function checks against existing players
		creator = _creator
		name = _name
		create_time = str(int(time.time()))
		owner = creator
		stamp = wmath.stamp()
		seed = creator + ":" + name + ":" + create_time + ":" + stamp
		hash = wu.whash(seed)
		wu.log(conf.text_new_wallet % (seed, hash))

class Cryptosystem:
	total_willcoin = 0
	reserve = 0
	bank = Wallet(_creator = conf.administration, _name = conf.bank_name)
	auction = [] # This isn't a wallet because there are no willcoin associated with it.
	players = {}
	tokens = {} # The actual tokens, not just the hashes
	wallets = {} # The actual wallets, not just the hashes
	def __init__ (self, _location = None, _size = conf.default_cryptosystem_size):
		self.new_cryptosystem(_size)

	def new_cryptosystem (self, _size = conf.default_cryptosystem_size):
		total_willcoin = _size

def exec_command (command, permissions = conf.perm_ru):
	# This is the big command that looks at all of the commands
	command_tokens = command.split(conf.command_token_delimiter) # Not to be confused with tokens
	command_mainfix = command_tokens[0] # Like a prefix or a suffix, but the main word in a command
	if command_mainfix == conf.command_exit and permissions == conf.perm_su:
		return True # returns true to signal that exit was requested.
	elif command_mainfix == conf.command_fortune:
		wu.fortune()
	elif permissions == conf.perm_su:
		wu.log(conf.text_warning % (conf.ansi_error, conf.ansi_reset,
			conf.text_command_unknown % (command_mainfix)))
	return False
