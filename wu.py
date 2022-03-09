# acronym of will and utils

import datetime, hashlib, json, random, requests
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

def fortune ():
	# TODO this should be called with a Discord channel, for now just log it
	log(random.choice(conf.fortunes))
