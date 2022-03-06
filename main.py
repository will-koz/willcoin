#!/usr/bin/python3

import discord, random, threading
import conf, will

exit_requested = False

main_cs = will.Cryptosystem(_size = conf.default_cryptosystem_size)
# the main instance of the cryptosystem. Unless the bot is running multiple systems from the same
# server, there does not need to be an array of cryptosystems

# Create a thread for parsing local commands

def su_command (): # Super User command thread
	global exit_requested # Don't know why, but there needs to be a declaration of its globality.
	while not exit_requested:
		recieved_command = input()
		if random.random() < 0.1:
			exit_requested = True

local_thread = threading.Thread(target = su_command)
local_thread.start()
