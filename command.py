import conf

def get_command_from_string (target):
	# Really basic function to return a string only if it begins with the command token. Some
	# commands, like ones delivered by the local user, are not prefaced with the token, so it is
	# useful to isolate this.
	if target[0] != conf.command_character:
		return None
	else:
		return target[1:]

def exec_command (target):
	command_tokens = target.split(conf.command_token_delimiter) # Not to be confused with tokens
