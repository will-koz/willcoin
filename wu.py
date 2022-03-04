# acronym of will and utils

import datetime, hashlib
import conf

def log (message = "Test"):
	output_text = conf.ansi_dull + "[" + str(datetime.datetime.now()) + "] " + conf.ansi_reset
	output_text += message
	print(output_text)

def whash (input = ""):
	return hashlib.sha256(bytes(input, conf.byte_encoding)).hexdigest()
