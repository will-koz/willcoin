import json, jsonpickle, math, requests, time
import command, conf, wmath, wu

class Player:
	def __init__ (self, _name = None, _jsonobj = None):
		if _jsonobj == None:
			self.new_player(_name = _name)
		else:
			self.json_player(jsonobj = _jsonobj)

	def json_player (self, jsonobj):
		self.name = jsonobj["name"]
		self.wallets = jsonobj["wallets"].copy()
		self.created_wallets = jsonobj["created_wallets"].copy()
		self.created_tokens = jsonobj["created_tokens"].copy()
		wu.log(conf.text_loaded_player % (self.name))

	def new_player (self, _name):
		self.name = _name
		self.wallets = []
		self.created_wallets = []
		self.created_tokens = []
		wu.log(conf.text_new_player % (_name))

class Token:
	def __init__ (self, url, initwallet, creator = conf.anonymous,
		name = conf.default_token_name, jsonobj = None):
		if jsonobj == None:
			self.new_token(url, initwallet, _creator = creator, _name = name)
		else:
			self.json_token(_jsonobj = jsonobj)

	def json_token (self, _jsonobj):
		self.cost = _jsonobj["cost"]
		self.create_time = _jsonobj["create_time"]
		self.creator = _jsonobj["creator"]
		self.hash = _jsonobj["hash"]
		self.rarity = _jsonobj["rarity"]
		self.name = _jsonobj["name"]
		self.owner = _jsonobj["owner"]
		self.seed = _jsonobj["seed"]
		self.stamp = _jsonobj["stamp"]
		self.url = _jsonobj["url"]
		wu.log(conf.text_loaded_token % (self.hash))

	def new_token (self, _url, _initwallet,
		_creator = conf.anonymous, _name = conf.default_token_name):
		self.cost = 0
		self.create_time = str(int(time.time()))
		self.creator = _creator
		self.rarity = wmath.getrarity()
		self.name = _name
		self.owner = _initwallet # The owner field is populated by a wallet hash, not a player
		self.stamp = wmath.stamp()
		self.url = _url

		self.seed = conf.seed_template % (self.creator, self.name, self.create_time, self.stamp)
		self.hash = wu.whash(self.seed)
		wu.log(conf.text_new_token % (self.seed, self.hash))

class Wallet:
	def __init__ (self, creator = conf.anonymous, name = conf.default_wallet_name, jsonobj = None):
		if jsonobj == None:
			self.new_wallet(_creator = creator, _name = name)
		else:
			self.json_wallet(_jsonobj = jsonobj)

	def json_wallet (self, _jsonobj):
		self.coins = _jsonobj["coins"]
		self.create_time = _jsonobj["create_time"]
		self.creator = _jsonobj["creator"]
		self.hash = _jsonobj["hash"]
		self.name = _jsonobj["name"]
		self.owner = _jsonobj["owner"]
		self.seed = _jsonobj["seed"]
		self.stamp = _jsonobj["stamp"]
		self.tokens = _jsonobj["tokens"].copy()
		wu.log(conf.text_loaded_wallet % (self.hash))

	def new_wallet (self, _creator = conf.anonymous, _name = conf.default_wallet_name):
		# If new_wallet is called, it is assumed that it is okay to create. i.e. if there is another
		# wallet owned by the player with the same name it is fine to create another one.
		self.coins = 0
		self.create_time = str(int(time.time()))
		self.creator = str(_creator)
		self.name = _name
		self.stamp = wmath.stamp()
		self.tokens = []

		self.owner = self.creator
		self.seed = conf.seed_template % (str(self.creator), \
			self.name, self.create_time, self.stamp)
		self.hash = wu.whash(self.seed)
		wu.log(conf.text_new_wallet % (self.seed, self.hash))

class Cryptosystem:
	def __init__ (self, _location):
		try:
			self.load_cryptosystem(_location)
		except FileNotFoundError:
			self.new_cryptosystem()

	# These next two functions have to do with saving and loading the cryptosystem. I don't know why
	# I felt the need to document that; it's pretty obvious

	def save_cryptosystem (self):
		output_file = open(conf.json_file, conf.json_file_mode)
		output_file.write(jsonpickle.encode(self))
		output_file.close()
		wu.log(conf.text_save)

	def load_cryptosystem (self, loc = conf.json_file):
		file = open(loc)
		jsonobject = json.load(file)
		file.close()
		self.json_cryptosystem(jsonobject)
		wu.log(conf.text_loaded_cryptosystem)

	def check_player_has_wallet (self, player_name, wallet_name):
		# I could probably save hundreds of hours over the course of the lifetime of a bot if I
		# actually used this function instead of reimplimenting it every time.
		player_name = str(player_name)
		if len(self.players[player_name].wallets) == 0:
			# Don't need to bother checking, the player doesn't have any wallets
			return False
		wallet_array = self.players[player_name].wallets
		for i in wallet_array:
			if self.wallets[i].name == wallet_name:
				return True
		return False

	def json_cryptosystem (self, jsonobj):
		# I don't feel like this needs to be logged because this will be called exactly once and is
		# already logged elsewhere.
		self.total_willcoin = jsonobj["total_willcoin"]
		self.reserve = jsonobj["reserve"]
		self.auction = jsonobj["auction"].copy()
		self.bank = jsonobj["bank"]
		self.players = {}
		self.tokens = {}
		self.wallets = {}
		for player in jsonobj["players"]:
			self.players[jsonobj["players"][player]["name"]] = \
				Player(_jsonobj = jsonobj["players"][player])
		for token in jsonobj["tokens"]:
			self.tokens[jsonobj["tokens"][token]["hash"]] = \
				Token(None, None, jsonobj = jsonobj["tokens"][token])
		for wallet in jsonobj["wallets"]:
			self.wallets[jsonobj["wallets"][wallet]["hash"]] = \
				Wallet(jsonobj = jsonobj["wallets"][wallet])

	def new_cryptosystem (self, _size = conf.default_cryptosystem_size):
		# This is for creating a cryptosystem, not loading one.
		wu.log(conf.text_new_cryptosystem)
		self.total_willcoin = _size
		self.reserve = 0
		self.auction = []
		self.players = {}
		self.tokens = {} # The actual tokens, not just the hashes
		self.wallets = {} # The actual wallets, not just the hashes

		bank_wallet = Wallet(creator = conf.administration, name = conf.bank_name)
		self.bank = bank_wallet.hash

		self.wallets[bank_wallet.hash] = bank_wallet
		self.wallets[self.bank].coins = self.total_willcoin

	def player_init (self, name):
		# This should be called regardless of if the player exists, just to make sure, so the first
		# line makes sure they don't already exist.
		if not str(name) in self.players:
			self.players[str(name)] = Player(str(name))
		# If you are crazy enough to actually read through the codebase and check if this could be
		# used in other functions, please file an issue.

	def get_account_coin(self, player_name):
		# This function goes through a players wallets and returns a sum of the coins
		coins = 0
		for i in self.players[player_name].wallets:
			coins += self.wallets[i].coins
		return coins

	async def get_account_info (self, player_name, message):
		# As accounts get really big, it might be a good idea to limit some of these things
		try:
			working_target_user = self.players[player_name]
		except KeyError:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_target_user_not_found % (player_name), title = ""))
			wu.log(conf.text_target_user_not_found % (player_name))
			return
		wallet_sum = self.get_account_coin(player_name) # player init is done in here
		wallets_num = len(self.players[player_name].wallets)
		cwallets_num = len(self.players[player_name].created_wallets)
		wallet_text = ""
		counter = 1
		for wallet in working_target_user.wallets:
			working_wallet = self.wallets[wallet]
			if counter != 1:
				wallet_text += "\n"
			wallet_text += conf.text_template_wallet % (counter, working_wallet.name, conf.symbol, \
				working_wallet.coins, working_wallet.owner, working_wallet.hash)
			subcounter = 1
			for token in working_wallet.tokens:
				target_token = self.tokens[token]
				wallet_text += "\n"
				wallet_text += conf.text_template_sub_token % (subcounter, target_token.name, \
					conf.symbol, target_token.cost, target_token.hash)
				subcounter += 1
			counter += 1
		return_string = conf.text_account_info % (cwallets_num, wallets_num, wallet_sum, \
			wallet_text)
		return return_string

	async def account_top (self, message):
		# A nice, bloated, way to give the top users / wallets / tokens back to users
		players = sorted(self.players.items(), reverse = True, \
			key = lambda item : self.get_account_coin(item[1].name))[:conf.ls_amount]
		wallets = sorted(self.wallets.items(), reverse = True, \
			key = lambda item : self.wallets[item[1].hash].coins)[:conf.ls_amount]
		tokens = sorted(self.tokens.items(), reverse = True, \
			key = lambda item : self.tokens[item[1].hash].cost)[:conf.ls_amount]
		player_text = ""
		counter = 1
		for player in players:
			if counter != 1:
				player_text += "\n"
			player_text += conf.text_template_player % (counter, player[1].name, conf.symbol, \
				self.get_account_coin(player[1].name))
			counter += 1
		wallet_text = ""
		counter = 1
		for wallet in wallets:
			if counter != 1:
				wallet_text += "\n"
			wallet_text += conf.text_template_wallet % (counter, wallet[1].name, conf.symbol, \
				wallet[1].coins, wallet[1].owner, wallet[1].hash)
			counter += 1
		token_text = ""
		counter = 1
		for token in tokens:
			if counter != 1:
				token_text += "\n"
			token_text += conf.text_template_token % (counter, token[1].name, conf.symbol, \
				token[1].cost, token[1].hash)
			counter += 1
		final_text = conf.text_template_account % (player_text, wallet_text, token_text)
		await message.channel.send(embed = wu.gen_willcoin_embed(final_text, \
			title = conf.text_top_accounts))
		wu.log(conf.text_account_top % (conf.command_character, message.author))

	async def auction_ls (self, message):
		# Named auction_ls because auction is already used in this class
		reply_text = ""
		counter = 1
		for i in self.auction:
			if counter != 1:
				reply_text += "\n"
			reply_text += conf.text_template_token % (counter, self.tokens[i].name, conf.symbol, \
				self.tokens[i].cost, i)
			counter += 1
		if reply_text == "":
			reply_text = conf.text_auction_none
		await message.channel.send(embed = wu.gen_willcoin_embed(reply_text, title = ""))
		wu.log(conf.text_auction % (conf.command_character, message.author))

	async def bank_ls (self, message):
		await self.wallet_ls(self.bank, message)

	async def give_coin (self, user, target_user, amount, message):
		self.player_init(user)
		amount = max(wmath.atoi(amount), 0)
		working_target_user = None
		working_wallet = ""
		working_target_wallet = ""
		try:
			working_target_user = self.players[target_user]
		except KeyError:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_target_user_not_found % (target_user), title = ""))
			wu.log(conf.text_target_user_not_found % (target_user))
			return
		for i in self.players[user].wallets:
			if self.wallets[i].coins >= amount:
				working_wallet = i
				break
		for i in working_target_user.wallets:
			working_target_wallet = i
			break
		if not working_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_not_found \
				% (amount), title = ""))
			wu.log(conf.text_wallet_not_found_w_user % (amount, user))
			return
		if not working_target_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_target_wallet_not_found, title = ""))
			wu.log(conf.text_target_wallet_not_found_w_user % (user))
			return
		self.wallets[working_wallet].coins -= amount
		self.wallets[working_target_wallet].coins += amount
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_give % \
			(conf.symbol, amount, target_user), title = ""))
		wu.log(conf.text_give_coin % (conf.symbol, amount, target_user))

	async def give_token (self, user, target_user, target_token, message):
		# Function used for give token to another player. I don't know what parts of this can be
		# optimized, and I'm not sure if I want to find out anymore.
		self.player_init(user)
		working_target_user = None
		working_token = ""
		working_target_wallet = ""
		try:
			working_target_user = self.players[target_user]
		except KeyError:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_target_user_not_found % (target_user), title = ""))
			wu.log(conf.text_target_user_not_found % (target_user))
			return
		for i in working_target_user.wallets:
			working_target_wallet = i
			break
		if not working_target_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_target_wallet_not_found % (target_wallet), title = ""))
			wu.log(conf.text_target_wallet_not_found % (target_wallet))
			return
		for walleth in self.players[user].wallets:
			for tokenh in self.wallets[walleth].tokens:
				if self.tokens[tokenh].name == target_token:
					working_token = tokenh
					break
					break
		if not working_token:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_target_token_not_found % (target_token), title = ""))
			wu.log(conf.text_target_token_not_found % (target_token))
			return
		self.wallets[self.tokens[working_token].owner].tokens.remove(working_token)
		self.wallets[working_target_wallet].tokens.append(working_token)
		self.tokens[working_token].owner = working_target_wallet
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_give_token % \
			(target_token, target_user), title = ""))
		wu.log(conf.text_give_token % (target_token, target_user))

	async def give_towallet (self, user, target_wallet, amount, message):
		self.player_init(user)
		amount = max(wmath.atoi(amount), 0)
		working_wallet = ""
		working_target_wallet = None
		for i in self.players[user].wallets:
			if self.wallets[i].coins >= amount:
				working_wallet = i
				break
		if not working_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_not_found % \
				(amount), title = ""))
			wu.log(conf.text_wallet_not_found_w_user % (amount, user))
			return
		try:
			working_target_wallet = self.wallets[target_wallet]
		except KeyError:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_target_wallet_not_found, title = ""))
			wu.log(conf.text_target_wallet_not_found_w_user % (user))
			return
		self.wallets[working_wallet].coins -= amount
		working_target_wallet.coins += amount
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_give_towallet % \
			(conf.symbol, amount, target_wallet), title = ""))
		wu.log(conf.text_give_towallet % (conf.symbol, amount, target_wallet))

	def reserve_coins (self, amount = conf.default_reserve_amount):
		# Used client side to put coins into the reserve.
		amount = wu.wint(amount)
		amount = min(self.wallets[self.bank].coins, amount)
		self.wallets[self.bank].coins -= amount
		self.reserve += amount
		wu.log(conf.text_reserve_reserve % (amount, self.reserve, self.wallets[self.bank].coins))

	async def token_msg (self, hash, mc):
		working_token = self.tokens[hash]
		title = conf.text_token_title % (working_token.name, working_token.rarity)
		body = conf.text_token_body % (working_token.creator, working_token.create_time, \
			conf.symbol, working_token.cost)
		footer = conf.text_token_footer % (working_token.seed, working_token.hash)
		await mc.send(embed = wu.gen_willcoin_embed(body, title = title, \
			img = working_token.url, foot = footer))

	async def token_ls (self, identifier, message):
		hash = ""
		try:
			hash = self.tokens[identifier].hash
		except:
			self.player_init(message.author)
			for i in self.players[str(message.author)].created_tokens:
				if self.tokens[i].name == identifier:
					hash = self.tokens[i].hash
		if hash == "":
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_not_found % \
				(identifier), title = ""))
			wu.log(conf.text_token_not_found % (identifier))
		else:
			await self.token_msg(hash, message.channel)

	async def token_buy (self, user, token, message):
		self.player_init(user)
		working_token = ""
		for tokenh in self.auction:
			if tokenh == token:
				working_token = tokenh
				break
		if working_token == "":
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_not_found % \
				(token), title = ""))
			wu.log(conf.text_token_not_found % (token))
			return
		if not working_token in self.auction:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_token_not_in_auction % (token), title = ""))
			wu.log(conf.text_token_not_in_auction % (token))
			return
		working_wallet = None
		for walleth in self.players[user].wallets:
			if self.wallets[walleth].coins >= self.tokens[working_token].cost:
				working_wallet = self.wallets[walleth]
				break
		if not working_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_not_found % \
				(self.tokens[working_token].cost), title = ""))
			wu.log(conf.text_wallet_not_found % (self.tokens[working_token].cost))
			return
		working_wallet.tokens.append(working_token)
		self.wallets[self.tokens[working_token].owner].tokens.remove(token)
		working_wallet.coins -= self.tokens[working_token].cost
		self.wallets[self.tokens[working_token].owner].coins += self.tokens[working_token].cost
		self.tokens[working_token].owner = working_wallet.hash
		self.auction.remove(working_token)
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_buy % \
			(self.tokens[working_token].name), title = ""))
		wu.log(conf.text_token_buy % (self.tokens[working_token].name))

	async def token_mint (self, mint_name, message):
		# This is a convoluted process, so if you are looking over the code and find an issue / find
		# an exploit, feel free to file an issue.
		url = ""
		initwallet = self.bank
		async for m in message.channel.history(limit = conf.history_limit):
			# Sorry for the naming scheme of m for message
			if m.author.name == message.author.name and m.attachments:
				url = m.attachments[0].url
				break
		if url == "":
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_token_attachment_unknown, title = ""))
			return
		working_token = Token(url, initwallet, creator = str(message.author), name = mint_name)
		self.tokens[working_token.hash] = working_token
		self.wallets[working_token.owner].tokens.append(working_token.hash)
		if working_token.owner == self.bank:
			self.auction.append(working_token.hash)
		self.player_init(working_token.creator)
		self.players[working_token.creator].created_tokens.append(working_token.hash)
		await self.token_msg(working_token.hash, message.channel)

		# This part is for the assigning of coins to minted tokens
		working_wallet = None # Initialize it because I don't know about variable scopes in python
		if len(self.players[working_token.creator].wallets):
			working_wallet = self.wallets[self.players[working_token.creator].wallets[0]]
		else:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_mint_warning, \
				title = ""))
			wu.log(conf.text_token_mint_warning)
			return
		generated_coins = math.ceil(self.wallets[self.bank].coins / conf.return_diminish_factor)
		self.wallets[self.bank].coins -= generated_coins
		working_wallet.coins += generated_coins

	async def token_sell (self, user, token, amount, message):
		# Selling a token does not immediately get the associated number of coins, but it puts a
		# token to auction, and is called with an amount of coins to set the price.
		self.player_init(user)
		working_token = ""
		for walleth in self.players[user].wallets:
			for tokenh in self.wallets[walleth].tokens:
				if self.tokens[tokenh].name == token:
					working_token = tokenh
					break
					break
		if working_token == "":
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_not_found % \
				(token), title = ""))
			wu.log(conf.text_token_not_found % (token))
			return
		if not working_token in self.auction:
			self.auction.append(working_token)
		self.tokens[working_token].cost = max(wmath.atoi(amount), 0)
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_sell % (token), \
			title = ""))
		wu.log(conf.text_token_sell % (token))

	async def token_unsell (self, user, token, message):
		# If you decide you like a token after all, or if you want to jack up the price of a token,
		# then this might be the command for you.
		self.player_init(user)
		working_token = ""
		for walleth in self.players[user].wallets:
			for tokenh in self.wallets[walleth].tokens:
				if self.tokens[tokenh].name == token:
					working_token = tokenh
					break
					break
		if working_token == "":
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_not_found % \
				(token), title = ""))
			wu.log(conf.text_token_not_found % (token))
			return
		if working_token in self.auction:
			self.auction.remove(working_token)
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_unsell % \
				(token), title = ""))
			wu.log(conf.text_token_unsell % (token))
		else:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_token_not_in_auction % (token), title = ""))
			wu.log(conf.text_token_not_in_auction % (token))

	async def token_unown (self, user, token, message):
		# I don't know why someone would use this, but I coded it in anyway. The general idea is
		# that if, for some reason, someone wanted to get rid of a token, this would be how they do
		# it.
		self.player_init(user)
		working_token = ""
		working_wallet = None
		working_target_wallet = self.wallets[self.bank]
		for walleth in self.players[user].wallets:
			for tokenh in self.wallets[walleth].tokens:
				if self.tokens[tokenh].name == token:
					working_token = tokenh
					break
					break
		if working_token == "":
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_not_found % \
				(token), title = ""))
			wu.log(conf.text_token_not_found % (token))
			return
		if not working_token in self.auction:
			# If it gets own by the bank again, it can automatically go into auction.
			self.auction.append(working_token)
		working_target_wallet.tokens.append(working_token)
		working_wallet = self.wallets[self.tokens[working_token].owner]
		working_wallet.tokens.remove(working_token)
		self.tokens[working_token].owner = self.bank
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_unown % (token), \
			title = ""))
		wu.log(conf.text_token_unown % (token))

	def unreserve_coins (self, amount = conf.default_reserve_amount, target_wallet = ""):
		# I don't know how, after so many commits, this function ended up down here, but it is like
		# the same thing as reserve, but in reverse. Reverse reserve, as it were.
		try:
			target_wallet = self.wallets[target_wallet].hash
		except:
			target_wallet = self.bank
		amount = wu.wint(amount)
		amount = min(self.reserve, amount)
		self.reserve -= amount
		self.wallets[target_wallet].coins += amount
		wu.log(conf.text_reserve_unreserve % (amount, target_wallet, self.reserve, \
			self.wallets[self.bank].coins))

	async def wallet_destroy (self, owner, name, message):
		# owner is the owner of the wallet to be destroyed, name is the name of the wallet to be
		# destroyed, and message is the message that requested the wallet to be destroyed.
		self.player_init(str(owner)) # make sure the player exists, to stop errors down the line
		# I know, above line is janky considering how the rest of the system works, but I think I
		# already said somewhere that there is not a style guide for this project.
		working_wallet = None
		target_wallet = None # The wallet that all coin and tokens will be moved to
		for i in self.players[str(owner)].wallets:
			if self.wallets[i].name == name:
				working_wallet = self.wallets[i]
			elif target_wallet == None:
				target_wallet = self.wallets[i]
			if working_wallet != None and target_wallet != None:
				break
		if working_wallet == None or target_wallet == None:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_wallet_destroy_error, title = ""))
			wu.log(conf.text_wallet_destroy_error)
			return
		moved_coins = working_wallet.coins
		# By storing this in a seperate variable, it'll prevent infinite money glitches, hopefully
		working_wallet.coins -= moved_coins
		target_wallet.coins += moved_coins
		while working_wallet.tokens:
			# TEMP think this is working now, but I want to leave this as a bookmark in case there
			# are any bugs.
			working_token = working_wallet.tokens.pop()
			self.tokens[working_token].owner = target_wallet.hash
			target_wallet.tokens.append(working_token)

		# remove from owner wallets, then from creator wallets, then from cryptosystem wallets
		self.players[working_wallet.creator].created_wallets.remove(working_wallet.hash)
		self.players[working_wallet.owner].wallets.remove(working_wallet.hash)
		del self.wallets[working_wallet.hash]
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_destroy, \
			title = ""))
		wu.log(conf.text_wallet_destroy)

	async def wallet_give (self, user, name, target_user, message):
		# Give name, owned by user to target_user
		self.player_init(user)
		working_user = self.players[user]
		working_target_user = None
		try:
			working_target_user = self.players[target_user]
		except KeyError:
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_target_user_not_found % (target_user), title = ""))
			wu.log(conf.text_target_user_not_found % (target_user))
			return
		working_wallet = None
		for i in working_user.wallets:
			if self.wallets[i].name == name:
				working_wallet = i
				break
		if not working_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_not_found % \
				(name), title = ""))
			return
		working_user.wallets.remove(working_wallet)
		working_target_user.wallets.append(working_wallet)
		self.wallets[working_wallet].owner = str(working_target_user)
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_give % (name, \
			target_user), title = ""))
		wu.log(conf.text_wallet_give % (name, target_user))

	async def wallet_main (self, user, name, message):
		# Designates a specific wallet as the main wallet for a user
		self.player_init(user)
		working_wallet = ""
		for wallet in self.players[user].wallets:
			if self.wallets[wallet].name == name:
				working_wallet = wallet
				break
		if working_wallet == "":
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_wallet_not_found_generic % (name), title = ""))
			wu.log(conf.text_wallet_not_found_generic % (name))
			return
		self.players[user].wallets.remove(working_wallet)
		self.players[user].wallets.insert(0, working_wallet)
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_mained % (name, \
			user), title = ""))
		wu.log(conf.text_wallet_mained % (name, user))

	async def wallet_move (self, user, wallet, target_wallet, amount, message):
		# Move the contents of one wallet to another wallet.
		self.player_init(user)
		working_wallet = None
		working_target_wallet = None
		for walleth in self.players[user].wallets:
			if self.wallets[walleth].name == wallet and not working_wallet:
				working_wallet = self.wallets[walleth]
			elif self.wallets[walleth].name == target_wallet and not working_target_wallet:
				working_target_wallet = self.wallets[walleth]
			if working_wallet and working_target_wallet:
				break
		if not working_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_move_error % \
				(wallet), title = ""))
			wu.log(conf.text_wallet_move_error % (wallet))
			return
		if not working_target_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_move_error % \
				(target_wallet), title = ""))
			wu.log(conf.text_wallet_move_error % (target_wallet))
			return
		amount = min(working_wallet.coins, wmath.atoi(amount))
		working_wallet.coins -= amount
		working_target_wallet.coins += amount
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_move % \
			(conf.symbol, amount, target_wallet), title = ""))
		wu.log(conf.text_wallet_move % (conf.symbol, amount, target_wallet))

	async def wallet_movet (self, user, wallet, target_wallet, token, message):
		# Move a specific token from a wallet to another wallet.
		self.player_init(user)
		working_wallet = None
		working_target_wallet = None
		working_token = ""
		for walleth in self.players[user].wallets:
			if self.wallets[walleth].name == wallet and not working_wallet:
				working_wallet = self.wallets[walleth]
			elif self.wallets[walleth].name == target_wallet and not working_target_wallet:
				working_target_wallet = self.wallets[walleth]
			if working_wallet and working_target_wallet:
				break
		if not working_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_move_error % \
				(wallet), title = ""))
			wu.log(conf.text_wallet_move_error % (wallet))
			return
		if not working_target_wallet:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_move_error % \
				(target_wallet), title = ""))
			wu.log(conf.text_wallet_move_error % (target_wallet))
			return
		for tokenh in working_wallet:
			if self.tokens[tokenh].name == token:
				working_token = tokenh
				break
		if not working_token:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_token_not_found % \
				(token), title = ""))
			wu.log(conf.text_token_not_found % (token))
			return
		working_wallet.tokens.remove(working_token)
		working_target_wallet.tokens.append(working_token)
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_movet % (token, \
			target_wallet), title = ""))
		wu.log(conf.text_wallet_movet % (token, target_wallet))

	async def wallet_msg (self, hash, mc):
		working_wallet = self.wallets[hash]
		title = conf.text_wallet_title % (working_wallet.name, working_wallet.owner)
		body = conf.text_wallet_body % (working_wallet.creator, working_wallet.create_time, \
			conf.symbol, working_wallet.coins)
		# This should be limited if performance is an issue, or people make really large wallets
		counter = 1
		for token in working_wallet.tokens:
			if counter != 1:
				body += "\n"
			body += conf.text_template_sub_token % (counter, self.tokens[token].name, conf.symbol, \
				self.tokens[token].cost, self.tokens[token].hash)
			counter += 1
		footer = conf.text_wallet_footer % (working_wallet.seed, working_wallet.hash)
		await mc.send(embed = wu.gen_willcoin_embed(body, title = title, foot = footer))

	async def wallet_ls (self, identifier, message):
		hash = ""
		try:
			hash = self.wallets[identifier].hash
		except:
			self.player_init(str(message.author))
			for i in self.players[str(message.author)].created_wallets:
				if self.wallets[i].name == identifier:
					hash = self.wallets[i].hash
		if hash == "":
			# Shameless reuse of move text
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_movet % \
				(identifier), title = ""))
			wu.log(conf.text_wallet_movet % (identifier))
		else:
			await self.wallet_msg(hash, message.channel)

	async def wallet_init (self, creator, name, message):
		# Create a new wallet, if you couldn't tell
		self.player_init(creator)
		if self.check_player_has_wallet(creator, name):
			creator_name = creator.name
			await message.channel.send(embed = wu.gen_willcoin_embed( \
				conf.text_wallet_already_exists % (creator_name, name), title = ""))
			return
		working_wallet = Wallet(creator, name)
		self.wallets[working_wallet.hash] = working_wallet
		self.players[str(creator)].wallets.append(working_wallet.hash)
		self.players[str(creator)].created_wallets.append(working_wallet.hash)
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_new_wallet % \
			(working_wallet.seed, working_wallet.hash), title = ""))

async def exec_command (command, cryptosystem, client, message = None, permissions = conf.perm_ru):
	# This is the big function that looks at all of the commands
	# message is the variable for the message object. command is the variable for message.content
	if command == "":
		return False
	command_tokens = command.split(conf.command_token_delimiter) # Not to be confused with tokens
	command_mainfix = command_tokens[0] # Like a prefix or a suffix, but the main word in a command

	# If there is a good alternative to switch / case in python, I want to know it
	if command_mainfix == conf.command_account and permissions == conf.perm_ru:
		try:
			command_subfix = command_tokens[1]
			if command_subfix == conf.command_account_ls:
				embed_text = await cryptosystem.get_account_info(command_tokens[2], message)
				if embed_text:
					await message.channel.send(embed = wu.gen_willcoin_embed(embed_text, \
						title = conf.text_account_title % (command_tokens[2])))
			elif command_subfix == conf.command_account_top:
				await cryptosystem.account_top(message)
			else:
				await message.channel.send(embed = wu.gen_willcoin_embed( \
					conf.text_command_unknown % (command_subfix), title = ""))
		except IndexError:
			# Default to aliasing 'account' command to 'account ls [sender]'
			embed_text = await cryptosystem.get_account_info(str(message.author), message)
			if embed_text:
				await message.channel.send(embed = wu.gen_willcoin_embed(embed_text, \
					title = conf.text_account_title % (str(message.author))))
	elif command_mainfix == conf.command_auction and permissions == conf.perm_ru:
		await cryptosystem.auction_ls(message)
	elif command_mainfix == conf.command_bank and permissions == conf.perm_ru:
		await cryptosystem.bank_ls(message)
	elif command_mainfix == conf.command_exit and permissions == conf.perm_su:
		# This only exits out of one thread not all of them. One of the eventual goals is to remove
		# all running threads.
		return True # returns true to signal that exit was requested.
	elif command_mainfix == conf.command_fortune and permissions == conf.perm_ru:
		try:
			command_subfix = command_tokens[1]
			if command_subfix == conf.command_fortune_cat:
				await message.channel.send(embed = wu.gen_willcoin_embed("", title = "", \
					img = requests.get(conf.cat_loc).json()["file"]))
			elif command_subfix == conf.command_fortune_color:
				await wu.say_color_fortune(message)
			elif command_subfix == conf.command_fortune_wiki:
				await wu.say_wiki_fortune(message)
			else:
				await wu.say_fortune(message)
		except IndexError:
			await wu.say_fortune(message)
	elif command_mainfix == conf.command_give and permissions == conf.perm_ru:
		try:
			command_subfix = command_tokens[1]
			if command_subfix == conf.command_give_coin:
				await cryptosystem.give_coin(str(message.author), command_tokens[2], \
					command_tokens[3], message)
			elif command_subfix == conf.command_give_token:
				await cryptosystem.give_token(str(message.author), command_tokens[2], \
					command_tokens[3], message)
			elif command_subfix == conf.command_give_towallet:
				await cryptosystem.give_towallet(str(message.author), command_tokens[2], \
					command_tokens[3], message)
			elif command_subfix == conf.command_give_wallet:
				await cryptosystem.wallet_give(str(message.author), command_tokens[3], \
					command_tokens[2], message)
			else:
				await message.channel.send(embed = wu.gen_willcoin_embed( \
					conf.text_command_unknown % (command_subfix), title = ""))
		except IndexError:
			if message != None:
				await message.channel.send(embed = wu.gen_willcoin_embed( \
					conf.text_command_parseerror % (command) + conf.embed_delimiter + \
					conf.text_command_infoprompt % (command_mainfix), title = ""))
			else:
				wu.log(conf.text_command_parseerror % (command))
	elif command_mainfix == conf.command_info and permissions == conf.perm_ru:
		try:
			command_subfix = command_tokens[1]
			if command_subfix == conf.command_auction:
				await message.channel.send(embed = wu.gen_willcoin_embed(conf.info_auction, \
					title = ""))
			elif command_subfix == conf.command_bank:
				await message.channel.send(embed = wu.gen_willcoin_embed(conf.info_bank, title = \
					""))
			elif command_subfix == conf.command_fortune:
				await message.channel.send(embed = wu.gen_willcoin_embed(conf.info_fortune, \
					title = ""))
			elif command_subfix == conf.command_token:
				try:
					command_trifix = command_tokens[2]
					if command_trifix == conf.info_token_buy:
						pass
					else:
						await message.channel.send(embed = wu.gen_willcoin_embed(conf.info_token, \
							title = ""))
				except:
					await message.channel.send(embed = wu.gen_willcoin_embed(conf.info_token, \
						title = ""))
			else:
				await message.channel.send(embed = wu.gen_willcoin_embed(conf.info_none % \
					(command_subfix), title = ""))
		except IndexError:
			await message.channel.send(embed = wu.gen_willcoin_embed(conf.info_about, title = ""))
	elif command_mainfix == conf.command_reserve and permissions == conf.perm_su:
		try:
			cryptosystem.reserve_coins(command_tokens[1])
		except IndexError:
			cryptosystem.reserve_coins()
	elif command_mainfix == conf.command_save and permissions == conf.perm_su:
		cryptosystem.save_cryptosystem()
	elif command_mainfix == conf.command_token and permissions == conf.perm_ru:
		try:
			command_subfix = command_tokens[1]
			if command_subfix == conf.command_token_buy:
				await cryptosystem.token_buy(str(message.author), command_tokens[2], message)
			elif command_subfix == conf.command_token_ls:
				await cryptosystem.token_ls(command_tokens[2], message)
			elif command_subfix == conf.command_token_mint:
				await cryptosystem.token_mint(command_tokens[2], message)
			elif command_subfix == conf.command_token_sell:
				await cryptosystem.token_sell(str(message.author), command_tokens[2], \
					command_tokens[3], message)
			elif command_subfix == conf.command_token_unown:
				await cryptosystem.token_unown(str(message.author), command_tokens[2], message)
			elif command_subfix == conf.command_token_unsell:
				await cryptosystem.token_unsell(str(message.author), command_tokens[2], message)
			else:
				await message.channel.send(embed = wu.gen_willcoin_embed( \
					conf.text_command_unknown % (command_subfix), title = ""))
		except IndexError:
			if message != None:
				await message.channel.send(embed = wu.gen_willcoin_embed( \
					conf.text_command_parseerror % (command) + conf.embed_delimiter + \
					conf.text_command_infoprompt % (command_mainfix), title = ""))
			else:
				wu.log(conf.text_command_parseerror % (command))
	elif command_mainfix == conf.command_unreserve and permissions == conf.perm_su:
		try:
			cryptosystem.unreserve_coins(command_tokens[1], command_tokens[2])
		except IndexError:
			try:
				cryptosystem.unreserve_coins(command_tokens[1])
			except IndexError:
				cryptosystem.unreserve_coins()
	elif command_mainfix == conf.command_wallet:
		try:
			command_subfix = command_tokens[1]
			passed_name = command_tokens[2]
			if command_subfix == conf.command_wallet_destroy:
				await cryptosystem.wallet_destroy(message.author, passed_name, message)
			elif command_subfix == conf.command_wallet_give:
				await cryptosystem.wallet_give(str(message.author), passed_name, \
					command_tokens[3], message)
			elif command_subfix == conf.command_wallet_init:
				await cryptosystem.wallet_init(message.author, passed_name, message)
			elif command_subfix == conf.command_wallet_ls:
				await cryptosystem.wallet_ls(command_tokens[2], message)
			elif command_subfix == conf.command_wallet_main:
				await cryptosystem.wallet_main(str(message.author), passed_name, message)
			elif command_subfix == conf.command_wallet_move:
				await cryptosystem.wallet_move(str(message.author), passed_name, \
					command_tokens[3], command_tokens[4], message)
			elif command_subfix == conf.command_wallet_movet:
				await cryptosystem.wallet_movet(str(message.author), passed_name, \
					command_tokens[3], command_tokens[4], message)
			else:
				await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_command_unknown \
					% (command_subfix), title = ""))
		except IndexError:
			if message != None:
				await message.channel.send(embed = wu.gen_willcoin_embed( \
					conf.text_command_parseerror % (command) + conf.embed_delimiter + \
					conf.text_command_infoprompt % (command_mainfix), title = ""))
			else:
				wu.log(conf.text_command_parseerror % (command))
	elif permissions == conf.perm_su: # Default to logging unknown command for superusers
		wu.log(conf.text_warning % (conf.ansi_error, conf.ansi_reset,
			conf.text_command_unknown % (command_mainfix)))
	elif message != None:
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_command_unknown % \
			(command_mainfix), title = ""))
	return False

async def handle_message (client, message, cs):
	if message.author.id == client.user.id:
		return # delete this line. I dare you

	message_command = command.get_command_from_string(message.content)
	if message_command:
		await exec_command(message_command, cs, client, message = message)
