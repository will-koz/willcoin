# acronym of will and utils

import datetime, discord, hashlib, json, random, requests
import conf

def get_json (location):
	# Get JSON from either local storage or from the internet
	try:
		# Probably going to be local.
		return json.load(open(location))
	except FileNotFoundError:
		request = requests.get(location)
		while request.status_code == conf.request_not_found_code:
			request = requests.get(location)
		return json.loads(request.content.decode(conf.byte_encoding))

def log (message = "Test"):
	output_text = conf.text_log_time % (conf.ansi_dull,
		str(datetime.datetime.now()), conf.ansi_reset)
	output_text += conf.text_log_message % (message)
	print(output_text)

def whash (input = ""):
	return hashlib.sha256(bytes(input, conf.byte_encoding)).hexdigest()

def wint (x):
	try:
		return int(x)
	except ValueError:
		return 0

# --------------------------------------------------------------------------------------------------

def color_fortune ():
	return discord.Colour.random()

def fortune ():
	return random.choice(conf.fortunes)

def fortune_dump ():
	for i in conf.fortunes:
		print(i)

async def say_color_fortune (message):
	c = color_fortune()
	await message.channel.send(c)
	log(conf.text_fortune_color % (c, message.author))

async def say_fortune (message):
	f = fortune()
	await message.channel.send(f)
	log(conf.text_fortune % (f, message.author))

def gen_willcoin_embed (text, title = None):
	e = discord.Embed(color = color_fortune(), description = text, title = title)
	return e
