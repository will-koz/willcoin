# willcoin

Willcoin is a centralized Discord cryptosystem. (That's fancy talk for a bot that attaches numbers
to a user.) Go to [Installation](#Installation) to read about how to install your own willcoin
server, then **remember to read the notes about [Running](#Running)**.

![Willcoin logo](logo/logo_400x400.png)

## Installation

This is created on Linux Mint, a Debian based Linux distribution, and not on Windows or OSX. I would
recommend installing on Linux or in a Linux VM.

- Make sure you have a text editor. i.e. vim or emacs on your system, and that it is up to date.
- [Make sure `python` and `pip` are installed and up to date on your system.](https://www.python.org/downloads/)
- Run `make install`. This will ask about a cron job. I use
`@reboot /usr/bin/python3.9 /home/will/git/willcoin/main >> /home/will/git/willcoin/log.txt`
- Find an account with a bot token. The token goes in token.txt, which I am obviously not going to
add to this repo, which is why you should run the above command. This step and the next step is
documented [here](https://discordpy.readthedocs.io/en/stable/discord.html).
- Create a server that can serve as a testing server and invite the bot to that server. See above.
- Put your Discord bot token into token.txt, if you haven't already
- I would recommend changing the administrator field in conf.py, but it is up to you
- You can begin running with a command like `./main`, `./main >> log.txt`, or `./main >> log.txt &`

- To update, I think you can just do git pull and then run `make install` again

## Running

After each session with the server running, remember to run the server-side `save` command, or else
nothing from that session will be saved. To run, just use `./main`. You can also output to a log
with `./main >> log.txt`. If you are using crontab (which I recommend since this is still in beta),
use something like `@reboot /home/will/git/willcoin/main >> /home/will/git/willcoin/log.txt`.

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
- [x] Install script / install guide
- [x] '.bank' command (alias for .wallet ls [bank hash])
- [x] Fortune cat functions
  - [x] color
  - [x] make only fortune color a random color ; all others are red or something
  - [x] wikipedia
- [x] Create a systemd service (Update: looking at just using crontab, because more systems have it)
- [x] unreserve to specific wallet
- [x] make '.info' for commands
  - [x] about
  - [x] 'list' command
- [x] Save on shutdown

### Long Term
 - [ ] algorithms
   - [ ] automatically remove tokens from auction if they have been there too long
   - [ ] change 'account top' for tokens
   - [ ] cooldown for users
     - [ ] cooldown for minting tokens specifically
   - [ ] require '.give wallet' have at least 1 coin or 1 token
 - [x] alias 'help' to 'info' (as usual, file an issue if there are any problems)
 - [x] Change bot status
 - [ ] Figure out if [random.cat](http://random.cat) is 429ing me.
 - [ ] Get random content from reddit
 - [ ] Handle the bug where you can't destroy wallets with user brackets.
 - [ ] Make a readthedocs.io
 - [x] Make a logo
 - [ ] Make wu.log() output the associated user
 - [x] Move a 400px x 400px logo to logo/logo_400x400.png
 - [ ] Server-side utilities
   - [ ] '>announce' command
   - [ ] '>exit' command
   - [ ] '>reboot' command
 - [ ] use @'s for selecting players

## Thanks

<!-- Update as this grows: TODO -->
Thank you very much to: *donburi* for making a logo and *\*Person who makes a theme?\** for making a
theme
