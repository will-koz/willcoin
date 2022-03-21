# willcoin

Willcoin is a centralized Discord cryptosystem. (That's fancy talk for a bot that attaches numbers
to a user.)

## Installation

This is created on Linux Mint, a Debian based Linux distribution, and not on Windows or OSX. I would
recommend installing in Linux or in a Linux VM.

- Find an account with a bot token. The token goes in token.txt, which I am obviously not going to
add to this repo.
- Create a server that can serve as a testing server and invite the bot to that server
- Run `make install` <!-- TODO -->

<!-- TODO: write more of an Installation Guide -->

## TODO

- [x] Connect to Discord API
- [ ] Parse Commands, call functions with appropriate users and permissions
  - [ ] For some remaining commands, create formal functions
    - [ ] >wallet
      - [x] init
      - [ ] move
      - [ ] destroy
      - [ ] give
    - [ ] >account
      - [ ] ls
      - [ ] top
    - [ ] >give
	- [ ] >token
      - [ ] mint
      - [ ] unown
      - [ ] sell
    - [ ] >exit
    - [ ] >save
    - [ ] >reboot
    - [ ] >announce
    - [x] >reserve
    - [x] >unreserve
    - [x] >info
- [ ] Load data from external file
- [ ] Save data to external file
- [x] Thread Handling
- [ ] Fortune / Wikipedia API functions
- [ ] Redo logging and make all output text embeds

## Thanks
