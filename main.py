#!/usr/bin/python3

# This entire codebase was written over two main sections. In the first, it was spread out over a
# month or so, so there is not a formal style guide. In the second, I thought I would be able to do
# everything really quickly, but I copy and pasted a couple of times without making a function. If
# it isn't obvious already, this is the definition of legacy code. Read at your own risk.

import asyncio, atexit, discord, random, sys, threading
import conf, will, wu

exit_requested = False

main_cs = will.Cryptosystem(conf.json_file)
# the main instance of the cryptosystem. Unless the bot is running multiple systems from the same
# server, there does not need to be an array of cryptosystems
atexit.register(main_cs.save_cryptosystem)
# Not quite a formal exit function, but it'll handle unexpected shutdowns.

# Create the Discord Client

token = open(conf.token, conf.file_mode)
token = token.readline().strip()

class WillClient (discord.Client):
	async def on_ready (self):
		wu.log(conf.text_logged_in % (self.user))
		await wc.change_presence(activity = discord.Activity(type = \
			discord.ActivityType.listening, name = conf.status_name))

	async def on_message (self, message):
		global main_cs
		await will.handle_message(self, message, main_cs)

wc = WillClient()

# Create a thread for parsing local commands

async def local_command_function (): # Super User command thread
	wu.log(conf.text_local_command_thread)
	global exit_requested, wc # Don't know why, but there needs to be a declaration of its globality.
	while not exit_requested:
		recieved_command = input()
		# Nice way to remove the command character if it's there.
		if recieved_command != "" and recieved_command[0] == conf.command_character:
			recieved_command = recieved_command[1:]
		exit_requested = await will.exec_command(recieved_command, main_cs, client = wc, \
			permissions = 1)

def local_command_daemon ():
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	loop.run_until_complete(local_command_function())
	loop.run_until_complete(wc.close())
	loop.close()

local_thread = threading.Thread(target = local_command_daemon)
local_thread.start()

# Run the bot

wu.log(conf.text_running_bot)
wc.run(token)
