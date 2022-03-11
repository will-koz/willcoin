#!/usr/bin/python3

import asyncio, discord, random, sys, time
import conf, will, wu

exit_requested = False

main_cs = will.Cryptosystem(_size = conf.default_cryptosystem_size)
# the main instance of the cryptosystem. Unless the bot is running multiple systems from the same
# server, there does not need to be an array of cryptosystems

# Create a "thread" for parsing local commands

async def local_command_daemon (): # Super User command thread
	global exit_requested, wc # there needs to be a declaration of the globality.
	print("local_command_daemon")
	while not exit_requested:
		recieved_command = input()
		# Nice way to remove the command character:
		if recieved_command != "" and recieved_command[0] == conf.command_character:
			recieved_command = recieved_command[1:] # if it's there.
		await will.exec_command(recieved_command, main_cs, client = wc, permissions = 1)
		wu.log_dump()

# Create the Discord Client

token = open(conf.token, conf.file_mode)
token = token.readline().strip()

class WillClient (discord.Client):
	async def on_ready (self):
		print("Here")
		wu.log("Logged in as {0}!".format(self.user))
		asyncio.run(local_command_daemon())

	async def on_message (self, message):
		wu.log("Message from {0.author}: {0.content}".format(message))

wc = WillClient()
wc.run(token)
