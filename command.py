import conf

def get_command_from_string (target):
	# Really basic function to return a string only if it begins with the command token. Some
	# commands, like ones delivered by the local user, are not prefaced with the token, so it is
	# useful to isolate this.
	if target == "" or target[0] != conf.command_character:
		return None
	else:
		return target[1:]

# Other command parsing utilities will be put here if necessary.
