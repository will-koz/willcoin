#!/usr/bin/python3

import discord, random, sys, threading, time
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
		wu.log("Logged in as {0}!".format(self.user))

	async def on_message (self, message):
		wu.log("Message from {0.author}: {0.content}".format(message))

wc = WillClient()

# Create a thread for parsing local commands

def local_command_daemon (): # Super User command thread
	global exit_requested, wc # there needs to be a declaration of the globality.
	while not exit_requested:
		recieved_command = input()
		print(recieved_command)
		# Nice way to remove the command character:
		if recieved_command != "" and recieved_command[0] == conf.command_character:
			recieved_command = recieved_command[1:] # if it's there.
		will.exec_command(recieved_command, main_cs, client = wc, permissions = 1)
		wu.log_dump()

local_thread = threading.Thread(target = local_command_daemon)
local_thread.start()

# Finally run the client

wc.run(token)
