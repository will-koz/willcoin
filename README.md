# willcoin

Willcoin is a centralized Discord cryptosystem. (That's fancy talk for a bot that attaches numbers
to a user.) Go to [Installation](#Installation) to read about how to install your own willcoin
server, then **remember to read the [Notes](#Notes)**.

## Installation

This is created on Linux Mint, a Debian based Linux distribution, and not on Windows or OSX. I would
recommend installing on Linux or in a Linux VM.

- Run `make install`
- Find an account with a bot token. The token goes in token.txt, which I am obviously not going to
add to this repo, which is why you should run the above command. This step and the next step is
documented [here](https://discordpy.readthedocs.io/en/stable/discord.html).
- Create a server that can serve as a testing server and invite the bot to that server. See above.
- Put your Discord bot token into token.txt
- I would recommend changing the administrator field in conf.py, but it is up to you

<!-- TODO: write more of an Installation Guide -->

## Notes

After each session with the server running, remember to run the server-side `save` command, or else
nothing from that session will be saved.

## TODO

- [x] Connect to Discord API
- [x] Parse Commands, call functions with appropriate users and permissions
  - [x] For some remaining commands, create formal functions
    - [x] >wallet
	  - [x] movet
      - [x] give
      - [x] ls
      - [x] move
	  - [x] main
      - [x] destroy
      - [x] init
    - [x] >account
      - [x] ls
      - [x] top
    - [x] >give
	  - [x] coin
	  - [x] token
	  - [x] towallet
	- [x] >auction
	- [x] >token
	  - [x] buy
	  - [x] unsell
      - [x] mint
	  - [x] ls
      - [x] sell
      - [x] unown
    - [x] >save
    - [x] >reserve
    - [x] >unreserve
    - [x] >info
- [x] Load data from external file
- [x] Save data to external file
- [x] Thread Handling
- [x] Redo logging
- [x] make all output text embeds with no title
- [x] grep -r TODO TEMP (counting this as done because all of the remaining are on this list IIRC)
- [x] grep awaits in front of channel.sends

### Important but unnecessary:
- [x] alias 'give wallet' to 'wallet give'
- [ ] Install script / install guide
- [x] '.bank' command (alias for .wallet ls [bank hash])
- [x] Fortune cat functions
  - [x] color
  - [x] make only fortune color a random color ; all others are red or something
  - [x] wikipedia
- [ ] Create a systemd service (Update: looking at just using crontab, because more systems have it)
- [x] unreserve to specific wallet
- [ ] make '.info' for commands
  - [x] about
  - [ ] 'list' command
- [x] Save on shutdown

### Long Term
 - [ ] algorithms
   - [ ] automatically remove tokens from auction if they have been there too long
   - [ ] change 'account top' for tokens
   - [ ] cooldown for users
     - [ ] cooldown for minting tokens specifically
 - [ ] alias 'help' to 'info'
 - [x] Change bot status
 - [ ] Make a readthedocs.io
 - [ ] Make a logo
 - [ ] Make wu.log() output the associated user
 - [ ] Get random content from reddit
 - [ ] Server-side utilities
   - [ ] '>announce' command
   - [ ] '>exit' command
   - [ ] '>reboot' command
 - [ ] use @'s for selecting players

## Thanks

<!-- TODO -->
