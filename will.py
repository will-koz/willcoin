import time
import command, conf, wmath, wu

class Player:
	name = ""
	wallets = []
	created_wallets = []
	def __init__ (self, _name = None, _wallets = None):
		# Like many other classes, can be loaded in or created TODO
		self.new_player(_name = _name, _wallets = _wallets)

	def new_player (self, _name, _wallets = None):
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
		self.creator = _creator
		self.name = _name
		self.create_time = str(int(time.time()))
		self.stamp = wmath.stamp()
		# TODO change seed finder string
		self.seed = self.creator + ":" + self.name + ":" + self.create_time + ":" + self.stamp
		self.hash = wu.whash(self.seed)
		wu.log(conf.text_new_token % (self.seed, self.hash))

class Wallet:
	coins = 0
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
		# TODO make sure that this function checks against existing wallets
		self.creator = _creator
		self.name = _name
		self.create_time = str(int(time.time()))
		self.owner = self.creator
		self.stamp = wmath.stamp()
		# TODO change seed finder string
		self.seed = self.creator + ":" + self.name + ":" + self.create_time + ":" + self.stamp
		self.hash = wu.whash(self.seed)
		wu.log(conf.text_new_wallet % (self.seed, self.hash))

class Cryptosystem:
	total_willcoin = 0
	reserve = 0 # This isn't a wallet because there are no tokens associated with it
	bank = None
	auction = [] # This isn't a wallet because there are no willcoin associated with it.
	players = {}
	tokens = {} # The actual tokens, not just the hashes
	wallets = {} # The actual wallets, not just the hashes
	def __init__ (self, _location = None, _size = conf.default_cryptosystem_size):
		self.new_cryptosystem(_size)

	def check_player_has_wallet (self, player_name, wallet_name):
		if not player_name in self.players:
			# Don't need to bother checking, the player doesn't have any wallets
			return False
		wallet_array = self.players[player_name].created_wallets
		for i in wallet_array:
			if self.wallets[i].name == wallet_name:
				return True
		return False

	def new_cryptosystem (self, _size = conf.default_cryptosystem_size):
		# Read carefully: This is for creating a cryptosystem, not loading one.
		self.total_willcoin = _size
		# Initialize bank
		bank_wallet = Wallet(_creator = conf.administration, _name = conf.bank_name)
		self.wallets[bank_wallet.hash] = bank_wallet
		self.bank = bank_wallet.hash
		self.wallets[self.bank].coins = self.total_willcoin

	def player_init (self, name):
		# This should be called regardless of if the player exists, just to make sure, so the first
		# line makes sure they don't already exist.
		if not name in self.players:
			self.players[name] = Player()
			wu.log(conf.text_new_player % (name))

	def reserve_coins (self, amount = conf.default_reserve_amount):
		amount = wu.wint(amount)
		amount = min(self.wallets[self.bank].coins, amount)
		self.wallets[self.bank].coins -= amount
		self.reserve += amount
		wu.log(conf.text_reserve_reserve % (amount, self.reserve, self.wallets[self.bank].coins))

	def unreserve_coins (self, amount = conf.default_reserve_amount):
		amount = wu.wint(amount)
		amount = min(self.reserve, amount)
		self.reserve -= amount
		self.wallets[self.bank].coins += amount
		wu.log(conf.text_reserve_unreserve % (amount, self.reserve, self.wallets[self.bank].coins))

	async def wallet_init (self, creator, name, message):
		self.player_init(creator.name)
		if self.check_player_has_wallet(creator.name, name):
			creator_name = creator.name.split(conf.player_name_delimiter)[0]
			await message.channel.send(conf.text_wallet_already_exists % (creator_name, name))
			return
		working_wallet = Wallet(creator.name, name)
		self.wallets[working_wallet.hash] = working_wallet
		self.players[creator.name].wallets.append(working_wallet.hash)
		self.players[creator.name].created_wallets.append(working_wallet.hash)
		await message.channel.send(conf.text_new_wallet % (working_wallet.seed,
			working_wallet.hash))

async def exec_command (command, cryptosystem, client, message = None, permissions = conf.perm_ru):
	# This is the big function that looks at all of the commands
	# message is the variable for the message object. command is the variable for message.content
	if command == "":
		return False
	command_tokens = command.split(conf.command_token_delimiter) # Not to be confused with tokens
	command_mainfix = command_tokens[0] # Like a prefix or a suffix, but the main word in a command

	# If there is a good alternative to switch / case in python, I want to know it
	if command_mainfix == conf.command_exit and permissions == conf.perm_su:
		# TODO finish an exit function
		return True # returns true to signal that exit was requested.
	elif command_mainfix == conf.command_fortune:
		await wu.say_fortune(message)
	elif command_mainfix == conf.command_info and permissions == conf.perm_ru:
		try:
			command_subfix = command_tokens[1]
			if command_subfix == conf.command_fortune:
				await message.channel.send(conf.info_fortune)
			else:
				await message.channel.send(conf.info_none % (command_subfix))
		except IndexError:
			await message.channel.send(conf.info_about)
	elif command_mainfix == conf.command_reserve and permissions == conf.perm_su:
		try:
			cryptosystem.reserve_coins(command_tokens[1])
		except IndexError:
			cryptosystem.reserve_coins()
	elif command_mainfix == conf.command_unreserve and permissions == conf.perm_su:
		try:
			cryptosystem.unreserve_coins(command_tokens[1])
		except:
			cryptosystem.unreserve_coins()
	elif command_mainfix == conf.command_wallet:
		try:
			command_subfix = command_tokens[1]
			passed_name = command_tokens[2]
			if command_subfix == conf.command_wallet_init:
				await cryptosystem.wallet_init(message.author, passed_name, message)
			else:
				await message.channel.send(conf.text_command_unknown % (command_subfix))
		except IndexError:
			if message != None:
				await message.channel.send(conf.text_command_parseerror % (command))
				await message.channel.send(conf.text_command_infoprompt % (command_mainfix))
			else:
				wu.log(conf.text_command_parseerror % (command))
	elif permissions == conf.perm_su: # Default to logging unknown command for superusers
		wu.log(conf.text_warning % (conf.ansi_error, conf.ansi_reset,
			conf.text_command_unknown % (command_mainfix)))
	elif message != None:
		await message.channel.send(conf.text_command_unknown % (command_mainfix))
	return False

async def handle_message (client, message, cs):
	if message.author.id == client.user.id:
		return # delete this line. I dare you

	message_command = command.get_command_from_string(message.content)
	if message_command:
		await exec_command(message_command, cs, client, message = message)
