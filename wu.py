# acronym of will and utils

import datetime, discord, hashlib, json, random, requests
import conf, wmath

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
	# It turns out I made a copy of this in wmath.
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
	# Isn't called when the bot is run, just added the function so that make fortuned can be called
	# to see all of the fortunes and a couple of random possible rarities
	for i in conf.fortunes:
		print(i)
	for i in range(25):
		print(wmath.getrarity())

def gen_willcoin_embed (text, title = None, img = None, foot = None,
	color = discord.Colour.darker_gray()):
	e = discord.Embed(color = color, description = text, title = title)
	if foot:
		e.set_footer(text = foot)
	if img:
		e.set_image(url = img)
	return e

# A bunch of these are just fortune functions. You can also do fortune cat, but I was able to make
# that a one liner in will.exec_command

async def say_color_fortune (message):
	c = color_fortune()
	await message.channel.send(embed = gen_willcoin_embed(c, title = "", color = c))
	log(conf.text_fortune_color % (c, message.author))

async def say_fortune (message):
	f = fortune()
	await message.channel.send(f)
	log(conf.text_fortune % (f, message.author))

async def say_wiki_fortune (message):
	f = requests.get(conf.wiki_loc).json()["content_urls"]["desktop"]["page"]
	await message.channel.send(f)
	log(conf.text_fortune_wiki % (f, message.author))
