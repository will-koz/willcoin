#!/usr/bin/python3

import discord, hashlib, json
import will

main_cs = will.Cryptosystem(size = 2 ** 25)
# the main instance of the cryptosystem. Unless the bot is running multiple systems from the same
# server, there does not need to be an array of cryptosystems
