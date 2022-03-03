# acronym of will and utils

import datetime
import conf

def log (message = "Test"):
	output_text = conf.ansi_dull + "[" + str(datetime.datetime.now()) + "] " + conf.ansi_reset
	output_text += message
	print(output_text)
