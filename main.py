#!/usr/bin/python3

import discord, random, sys, threading
import conf, will

exit_requested = False

main_cs = will.Cryptosystem(_size = conf.default_cryptosystem_size)
# the main instance of the cryptosystem. Unless the bot is running multiple systems from the same
# server, there does not need to be an array of cryptosystems

# Create a thread for parsing local commands

def local_command_daemon (): # Super User command thread
	global exit_requested # Don't know why, but there needs to be a declaration of its globality.
	while not exit_requested:
		recieved_command = input()
		if recieved_command[0] == conf.command_character: # Nice way to remove the command character
			recieved_command = recieved_command[1:] # if it's there.
		exit_requested = will.exec_command(recieved_command, permissions = 1)

local_thread = threading.Thread(target = local_command_daemon)
local_thread.start()
