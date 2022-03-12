#!/usr/bin/python3

import discord, random, sys, threading
import conf, will, wu

exit_requested = False

main_cs = will.Cryptosystem(_size = conf.default_cryptosystem_size)
# the main instance of the cryptosystem. Unless the bot is running multiple systems from the same
# server, there does not need to be an array of cryptosystems

# Create the Discord Client

token = open(conf.token, conf.file_mode)
token = token.readline().strip()

class WillClient (discord.Client):
	async def on_ready (self):
		wu.log(conf.text_logged_in % (self.user))

	async def on_message (self, message):
		global main_cs
		await will.handle_message(self, message, main_cs)

wc = WillClient()

# Create a thread for parsing local commands

def local_command_daemon (): # Super User command thread
	global exit_requested, wc # Don't know why, but there needs to be a declaration of its globality.
	while not exit_requested:
		recieved_command = input()
		# Nice way to remove the command character:
		if recieved_command != "" and recieved_command[0] == conf.command_character:
			recieved_command = recieved_command[1:] # if it's there.
		exit_requested = will.exec_command(recieved_command, main_cs, client = wc, permissions = 1)

local_thread = threading.Thread(target = local_command_daemon)
local_thread.start()

# Run the bot

wc.run(token)
