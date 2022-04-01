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

	def new_player (self, _name):
		self.name = _name
		self.wallets = []
		self.created_wallets = []
		self.created_tokens = []

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
		wu.log("Loaded in " + self.hash)

	def new_wallet (self, _creator = conf.anonymous, _name = conf.default_wallet_name):
		# TODO make sure that this function checks against existing wallets
		# or maybe not. Ill think about it.
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

	def save_cryptosystem (self):
		output_file = open(conf.json_file, conf.json_file_mode)
		output_file.write(jsonpickle.encode(self))
		output_file.close()

	def load_cryptosystem (self, loc = conf.json_file):
		file = open(loc)
		jsonobject = json.load(file)
		file.close()
		self.json_cryptosystem(jsonobject)

	def check_player_has_wallet (self, player_name, wallet_name):
		if not player_name in self.players:
			# Don't need to bother checking, the player doesn't have any wallets
			return False
		wallet_array = self.players[player_name].created_wallets
		for i in wallet_array:
			if self.wallets[i].name == wallet_name:
				return True
		return False

	def json_cryptosystem (self, jsonobj):
		wu.log("Opening from file")
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
			wu.log(conf.text_new_player % (name))

	def get_account_coin(self, player_name):
		self.player_init(player_name)
		coins = 0
		for i in self.players[player_name].wallets:
			coins += self.wallets[i].coins
		return coins

	def get_account_info (self, player_name): # Sorry its not in perfect alphabetic order
		wallet_sum = self.get_account_coin(player_name) # player init is done in here
		wallets_num = len(self.players[player_name].wallets)
		cwallets_num = len(self.players[player_name].created_wallets)
		return_string = conf.text_account_info % (cwallets_num, wallets_num, wallet_sum)
		return return_string

	async def account_top (self, message):
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
				wallet[1].coins, wallet[1].hash)
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

	def reserve_coins (self, amount = conf.default_reserve_amount):
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
			for i in self.players[str(message.author)].created_tokens:
				if self.tokens[i].name == identifier:
					hash = self.tokens[i].hash
		if hash == "":
			# TODO: give this data to user
			pass
		else:
			await self.token_msg(hash, message.channel)

	async def token_buy (self, user, token, message):
		working_token = ""
		for tokenh in self.auction:
			if tokenh == token:
				working_token = tokenh
				break
		if working_token == "":
			return # TODO
		if not working_token in self.auction:
			return # TODO
		working_wallet = None
		for walleth in self.players[user].wallets:
			if self.wallets[walleth].coins >= self.tokens[working_token].cost:
				working_wallet = self.wallets[walleth]
				break
		if not working_wallet:
			return # TODO
		working_wallet.tokens.append(working_token)
		self.wallets[self.tokens[working_token].owner].tokens.remove(token)
		working_wallet.coins -= self.tokens[working_token].cost
		self.wallets[self.tokens[working_token].owner].coins += self.tokens[working_token].cost
		self.tokens[working_token].owner = working_wallet.hash
		self.auction.remove(working_token)
		# TODO Tell user

	async def token_mint (self, mint_name, message):
		# TODO make sure all of the returns have appropriate logging and message.sending
		url = ""
		initwallet = self.bank
		async for m in message.channel.history(limit = conf.history_limit):
			# Sorry for the naming scheme of m for message
			if m.author.name == message.author.name and m.attachments:
				url = m.attachments[0].url
				break
		if url == "":
			return # TODO
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
			return # TODO
		generated_coins = math.ceil(self.wallets[self.bank].coins / conf.return_diminish_factor)
		self.wallets[self.bank].coins -= generated_coins
		working_wallet.coins += generated_coins

	async def token_sell (self, user, token, amount, message):
		working_token = ""
		for walleth in self.players[user].wallets:
			for tokenh in self.wallets[walleth].tokens:
				if self.tokens[tokenh].name == token:
					working_token = tokenh
					break
					break
		if working_token == "":
			return # TODO
		if not working_token in self.auction:
			self.auction.append(working_token)
		self.tokens[working_token].cost = max(wmath.atoi(amount), 0)

	async def token_unown (self, user, token, message):
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
			return # TODO
		if not working_token in self.auction:
			self.auction.append(working_token)
		working_target_wallet.tokens.append(working_token)
		working_wallet = self.wallets[self.tokens[working_token].owner]
		working_wallet.tokens.remove(working_token)
		self.tokens[working_token].owner = self.bank

	def unreserve_coins (self, amount = conf.default_reserve_amount):
		amount = wu.wint(amount)
		amount = min(self.reserve, amount)
		self.reserve -= amount
		self.wallets[self.bank].coins += amount
		wu.log(conf.text_reserve_unreserve % (amount, self.reserve, self.wallets[self.bank].coins))

	async def wallet_destroy (self, owner, name, message):
		# owner is the owner of the wallet to be destroyed, name is the name of the wallet to be
		# destroyed, and message is the message that requested the wallet to be destroyed.
		self.player_init(str(owner)) # make sure the player exists, to stop errors down the line
		# TODO
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
			# TODO: give this warning back to user
			return # don't need to go any further
		moved_coins = working_wallet.coins
		# By storing this in a seperate variable, it'll prevent infinite money glitches, hopefully
		working_wallet.coins -= moved_coins
		target_wallet.coins += moved_coins
		while working_wallet.tokens:
			# TEMP come back later and determine if there needs to be more delicate handling of
			# transferred tokens
			target_wallet.tokens.append(working_wallet.tokens.pop())

		# remove from owner wallets, then from creator wallets, then from cryptosystem wallets
		self.players[working_wallet.creator].created_wallets.remove(working_wallet.hash)
		self.players[working_wallet.owner].wallets.remove(working_wallet.hash)
		del self.wallets[working_wallet.hash]
		# TODO log and tell user

	async def wallet_give (self, user, name, target_user, message):
		self.player_init(user)
		working_user = self.players[user]
		working_target_user = None
		try:
			working_target_user = self.players[target_user]
		except KeyError:
			await message.channel.send(conf.text_wallet_give_target_user_not_found % (target_user))
			return # TODO
		working_wallet = None
		for i in working_user.wallets:
			if self.wallets[i].name == name:
				working_wallet = i
				break
		if not working_wallet:
			return # TODO
		working_user.wallets.remove(working_wallet)
		working_target_user.wallets.append(working_wallet)
		self.wallets[working_wallet].owner = working_target_user
		# TODO give messages back to user

	async def wallet_main (self, user, name, message):
		working_wallet = ""
		for wallet in self.players[user].wallets:
			if self.wallets[wallet].name == name:
				working_wallet = wallet
				break
		if working_wallet == "":
			return # TODO
		self.players[user].wallets.remove(working_wallet)
		self.players[user].wallets.insert(0, working_wallet)
		await message.channel.send(embed = wu.gen_willcoin_embed(conf.text_wallet_mained % (name, \
			user), title = ""))

	async def wallet_move (self, user, wallet, target_wallet, amount, message):
		working_wallet = None
		working_target_wallet = None
		for walleth in self.players[user].wallets:
			if self.wallets[walleth].name == wallet and not working_wallet:
				working_wallet = self.wallets[walleth]
			elif self.wallets[walleth].name == target_wallet and not working_target_wallet:
				working_target_wallet = self.wallets[walleth]
			if working_wallet and working_target_wallet:
				break
		if not working_wallet or not working_target_wallet:
			return # TODO
		amount = min(working_wallet.coins, wmath.atoi(amount))
		working_wallet.coins -= amount
		working_target_wallet.coins += amount
		# TODO tell user

	async def wallet_movet (self, user, wallet, target_wallet, token, message):
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
		if not working_wallet or not working_target_wallet:
			return # TODO
		for tokenh in working_wallet:
			if self.tokens[tokenh].name == token:
				working_token = tokenh
				break
		if not working_token:
			return # TODO
		working_wallet.tokens.remove(working_token)
		working_target_wallet.tokens.append(working_token)
		# TODO tell user

	async def wallet_msg (self, hash, mc):
		working_wallet = self.wallets[hash]
		title = conf.text_wallet_title % (working_wallet.name, working_wallet.owner)
		body = conf.text_wallet_body % (working_wallet.creator, working_wallet.create_time, \
			conf.symbol, working_wallet.coins)
		# TODO: add list of tokens above
		counter = 1
		for token in working_wallet.tokens:
			body += conf.text_template_token % (counter, self.tokens[token].name, conf.symbol, \
				self.tokens[token].cost, self.tokens[token].hash)
			counter += 1
		footer = conf.text_wallet_footer % (working_wallet.seed, working_wallet.hash)
		await mc.send(embed = wu.gen_willcoin_embed(body, title = title, foot = footer))

	async def wallet_ls (self, identifier, message):
		hash = ""
		try:
			hash = self.wallets[identifier].hash
		except:
			for i in self.players[str(message.author)].created_wallets:
				if self.wallets[i].name == identifier:
					hash = self.wallets[i].hash
		if hash == "":
			# TODO: give this data to user
			pass
		else:
			await self.wallet_msg(hash, message.channel)

	async def wallet_init (self, creator, name, message):
		self.player_init(creator)
		if self.check_player_has_wallet(creator, name):
			creator_name = creator.name
			await message.channel.send(conf.text_wallet_already_exists % (creator_name, name))
			return
		working_wallet = Wallet(creator, name)
		self.wallets[working_wallet.hash] = working_wallet
		self.players[str(creator)].wallets.append(working_wallet.hash)
		self.players[str(creator)].created_wallets.append(working_wallet.hash)
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
	if command_mainfix == conf.command_account and permissions == conf.perm_ru:
		try:
			command_subfix = command_tokens[1]
			if command_subfix == conf.command_account_ls:
				embed_text = cryptosystem.get_account_info(command_tokens[2])
				await message.channel.send(embed = wu.gen_willcoin_embed(embed_text, \
					title = conf.text_account_title % (command_tokens[2])))
			elif command_subfix == conf.command_account_top:
				await cryptosystem.account_top(message)
			else:
				# TODO: give info back
				pass
		except IndexError:
			# Default to aliasing 'account' command to 'account ls [sender]'
			embed_text = cryptosystem.get_account_info(str(message.author))
			await message.channel.send(embed = wu.gen_willcoin_embed(embed_text, \
				title = conf.text_account_title % (str(message.author))))
	elif command_mainfix == conf.command_auction and permissions == conf.perm_ru:
		await cryptosystem.auction_ls(message)
	elif command_mainfix == conf.command_exit and permissions == conf.perm_su:
		# TODO finish an exit function
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
			else:
				await message.channel.send(conf.text_command_unknown % (command_subfix))
		except IndexError:
			await message.channel.send("TODO token thing")
	elif command_mainfix == conf.command_unreserve and permissions == conf.perm_su:
		try:
			cryptosystem.unreserve_coins(command_tokens[1])
		except:
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
				await message.channel.send(conf.text_command_unknown % (command_subfix))
		except IndexError:
			if message != None:
				await message.channel.send(embed = \
					wu.gen_willcoin_embed(conf.text_command_parseerror % (command) + \
					conf.embed_delimiter + conf.text_command_infoprompt % (command_mainfix)))
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
