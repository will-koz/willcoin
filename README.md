# willcoin

Willcoin is a centralized Discord cryptosystem. (That's fancy talk for a bot that attaches numbers
to a user.)

## Installation

This is created on Linux Mint, a Debian based Linux distribution, and not on Windows or OSX. I would
recommend installing in Linux or in a Linux VM.

- Run `make install` <!-- TODO -->
- Find an account with a bot token. The token goes in token.txt, which I am obviously not going to
add to this repo, which is why you should run the above command. This step and the next step is
documented [here](https://discordpy.readthedocs.io/en/stable/discord.html).
- Create a server that can serve as a testing server and invite the bot to that server. See above.
- Put your Discord bot token into token.txt

<!-- TODO: write more of an Installation Guide -->

## TODO

- [x] Connect to Discord API
- [x] Parse Commands, call functions with appropriate users and permissions
  - [ ] For some remaining commands, create formal functions
    - [x] >wallet
	  - [ ] movet
      - [x] give
      - [x] ls
      - [ ] move
	  - [x] main
      - [x] destroy
      - [x] init
    - [x] >account
      - [x] ls
      - [x] top
    - [ ] >give
	  - [ ] coin
	  - [ ] token
	  - [ ] wallet
	- [x] >auction
	- [x] >token
	  - [ ] buy
	  - [ ] unsell
      - [x] mint
	  - [x] ls
      - [ ] sell
      - [ ] unown
    - [x] >save
    - [x] >reserve
    - [x] >unreserve
    - [x] >info
- [x] Load data from external file
- [x] Save data to external file
- [x] Thread Handling
- [ ] Redo logging and make all output text embeds
- [ ] grep -r TODO TEMP

### Important but unnecessary:
- [ ] Install script
- [ ] '>announce' command
- [ ] '>exit' command
- [ ] '>reboot' command
- [x] Fortune cat functions
  - [x] color
  - [ ] make only fortune color a random color ; all others are red or something
  - [x] wikipedia
- [ ] Create a systemd service / unit
- [ ] make '>info' for commands

## Thanks

<!-- TODO -->
