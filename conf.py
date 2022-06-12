administration = "Admin"
administrator = "Will_ko#1244"
anonymous = "Anon"
bank_name = "BankOfWill"
byte_encoding = "utf-8"
cat_loc = "https://aws.random.cat/meow"
command_character = '.'
command_token_delimiter = ' '
default_cryptosystem_size = 2 ** 25
default_reserve_amount = 2 ** 10
default_stamp_size = 8
default_token_name = "NewToken"
default_wallet_name = "NewWallet"
embed_delimiter = " "
file_mode = "r"
history_limit = 20
json_file = "cryptosystem.json"
json_file_mode = "w"
ls_amount = 5
rarities = [
	("common", 100),
	("\"special\"", 75),
	("kinda cool", 45),
	("rare-ish", 20),
	("person who pays for WinRAR", 6),
	("legendary", 3),
	("uncommon", 1)
]
request_not_found_code = 429
return_diminish_factor = 40
seed_template = "%s:%s:%s:%s"
special_rarity = "This rarity shouldn't be possible if the random choice algorithm worked..."
stamp_values = "0123456789abcdef"
symbol = "\u20A9"
token = "token.txt"
wiki_loc = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

ansi_escape = "\033["
ansi_reset = ansi_escape + "0m"
ansi_dull = ansi_escape + "2m"
ansi_error = ansi_escape + "1;31m"

command_about = "about"
command_account = "account"
command_account_ls = "list"
command_account_top = "top"
command_auction = "auction"
command_bank = "bank"
command_exit = "exit"
command_fortune = "fortune"
command_fortune_cat = "cat"
command_fortune_color = "color"
command_fortune_wiki = "wiki"
command_give = "give"
command_give_coin = "coin"
command_give_token = "token"
command_give_towallet = "towallet"
command_give_wallet = "wallet"
command_help = "help"
command_info = "info"
command_ls = "list"
command_reserve = "reserve"
command_save = "save"
command_token = "token"
command_token_buy = "buy"
command_token_ls = "list"
command_token_mint = "mint"
command_token_sell = "sell"
command_token_unown = "unown"
command_token_unsell = "unsell"
command_unreserve = "unreserve"
command_wallet = "wallet"
command_wallet_destroy = "destroy"
command_wallet_give = "give"
command_wallet_init = "init"
command_wallet_ls = "list"
command_wallet_main = "main"
command_wallet_move = "move"
command_wallet_movet = "movet"

fortunes = [
	":(){:|:&};:",
	"\\*\\*Sample Fortune\\*\\*",
	"\u0D9E",
	"\u221E\u00B2 - 1 = (\u221E - 1)(\u221E + 1)",
	"\u222B(e ^ x)dx = e ^ x",
	"<PC Load Letter>",
	"2 + 2 = 5",
	"254ebc9d57cb06da5ea1bf685c7a04b0bfe9c808d5dcb5d093fc640f713dab9e",
	"Another day, another watermelon",
	"Back in my day, we walked uphill both ways.",
	"dQw4w9WgXcQ",
	"Epstein didn't kill himself.",
	"Everybody walk the dinosaur",
	"Feed the cows!",
	"Gentlemen, you can't fight in here! This is the War Room!",
	"Go Greendale!",
	"Have you actually met anyone from Nebraska?",
	"Hey you, you're finally awake",
	"HEYYEYAAEYAAAEYAEYAA",
	"Houston, we have a problem",
	"How do you beat the stab monster? Stabbing it just makes it stronger.",
	"https://en.wikipedia.org/wiki/Wikipedia",
	"https://twitter.com",
	"https://xkcd.com/1400",
	"I love the smell of napalm in the morning.",
	"I use Arch, btw",
	"Insane (in the Brain)",
	"It was a dark and stormy night.",
	"It's Morbin time.",
	"Just Lose It.",
	"Let's Say, Hypothetically",
	"Literally Animal Farm",
	"Loading: 142%",
	"Man Wonders If Speeding Ticket Just Karma For Going 120 MPH",
	"May the Force be with you",
	"Mug Moment",
	"Never give up. Never surrender",
	"Never mess with the sheep that steel wool comes from.",
	"Not PS5 Compatible ... yet",
	"Open the door, get on the floor",
	"Open the pod bay doors, HAL.",
	"Or is it?",
	"\*Out pizzas the hut\*",
	"Police police police police.",
	"Return to Monke",
	"Sponsored by Duolingo - \"Have you done your Spanish?\"",
	"Sponsored by Hooli",
	"sudo rm -rf / --no-preserve-root",
	"The existence of Purple Rain implies the existance of Red Rain.",
	"The palace of secret doors isn't that impressive. It's just one room.",
	"There is an impostor among us.",
	"This message will never appear on the splash screen, isn't that weird?",
	"Today's fortune: You're currently going through a difficult transition period called 'Life.'",
	"Toto, I've got a feeling we're not in Kansas anymore",
	"Vanilla Ice must've really been Under Pressure to create a new song",
	"What do you know about rolling down in the deep?",
	"What happened at 39.9054895\u00B0N, 116.395443\u00B0E?",
	"Where do birds go when it rains?",
	"while (true) return (true) ?: true;",
	"You can find Will Smith in the snow if you follow the fresh prints.",
	"zyxwvutsrqponmlkjihgfedcba"
]

info_about = """
Willcoin is a discord cryptosystem. Users can create any (realistic) number of wallets and they \
can assign coins to each one, as well as move tokens between wallets, which are like pieces of \
digital artwork. Users can get coins by minting tokens or trading coins.

Willcoin is open-source. The GitHub page is here: https://github.com/will-koz/willcoin
"""
info_account = """
The `""" + command_account + """` command is used to get information about accounts. Alone, it is \
an alias for `""" + command_character + command_account + command_token_delimiter + \
command_account_ls + """ [sender]`. There are two sub-commands:
- `""" + command_account + command_token_delimiter + command_account_ls + """`
- `""" + command_account + command_token_delimiter + command_account_top + """`
"""
info_account_list = """
Syntax: `""" + command_character + command_account + command_token_delimiter + command_account_ls \
+ command_token_delimiter + """[player]`
Return the account information about a player (specified by [player]).
"""
info_account_top = """
Syntax: `""" + command_character + command_account + command_token_delimiter + command_account_top \
+ """`
Return the top """ + str(ls_amount) + """ players, wallets and tokens. (The token algorithm is just \
how much coins the owner says it is worth. This is likely to change in the future.)
"""
info_auction = """
The `""" + command_auction + """` command displays some of the tokens that are at auction.
"""
info_bank = """
The `""" + command_bank + """` command displays the bank wallet. It is an alias for `""" + \
command_wallet + command_token_delimiter + command_wallet_ls + command_token_delimiter + \
"""[bank hash]`."""
info_fortune = """
The `""" + command_fortune + """` comand is used to get random content. It can be used to get a \
random unix fortune-like fortune. You can also use the following sub-commands to get specific \
random content:
- `""" + command_fortune + command_token_delimiter + command_fortune_cat + """` to get a random \
cat image
- `""" + command_fortune + command_token_delimiter + command_fortune_wiki + """` to get a random \
Wikipedia page
- `""" + command_fortune + command_token_delimiter + command_fortune_color + """` to get a random \
color in hex format. The border of the embed will also be that color
"""
info_general = """
Thanks for using `""" + command_character + command_info + """`. Willcoin is a Discord \
cryptosystem. (It's like a cryptocurrency, but I don't feel comfortable saying that quite yet, and \
it’s built on Discord). You can use the `""" + command_character + command_info + """` to get more \
information on commands, and you can use `""" + command_character + command_ls + """` to get a \
list of all commands.

The idea of the system is that each user can have any number of wallets, and wallets can be \
associated (or have) any number of the existing Willcoin and user generated tokens. At the \
beginning of the system, all of the coins are owned by the bank, but as users begin to mint tokens \
(which are pieces of art, or memes they have saved to their drives) the bank pays out coins, but \
at a decreasing rate.

All tokens will be owned by a wallet, and a wallet can have (in theory) any number of tokens. Each \
wallet and each token has a seed, made by some of the information determined when they are \
generated, and a hash (https://en.wikipedia.org/wiki/Hash_function), specifically generated using \
the sha256 hash algorithm (https://en.wikipedia.org/wiki/SHA-2).

To get information about a user, make sure they are a member of the cryptosystem, and use their \
name and discriminator (tag). As this project evolves one plan is to add @ing people, but that is \
not done yet.
"""
info_general_info = """
See `""" + command_character + command_info + command_token_delimiter + command_info + \
command_token_delimiter + command_info + """` for more information.
"""
info_give = """
The `""" + command_give + """` command is used to transfer coins, tokens, and wallets between \
users. With the exception of `""" + command_give + command_token_delimiter + \
command_give_towallet + """`, `""" + command_give + """` commands all have the target player as \
the first argument after the command.
- `""" + command_give + command_token_delimiter + command_give_coin + """`
- `""" + command_give + command_token_delimiter + command_give_token + """`
- `""" + command_give + command_token_delimiter + command_give_towallet + """`
- `""" + command_give + command_token_delimiter + command_give_wallet + """`
"""
info_give_coin = """
Syntax: `""" + command_character + command_give + command_token_delimiter + command_give_coin + \
command_token_delimiter + """[player]""" + command_token_delimiter + """[amount]`
Transfer an amount of coins (specified by [amount]) from one of your wallets to another player's \
(specified by [player]) main wallet.
"""
info_give_token = """
Syntax: `""" + command_character + command_give + command_token_delimiter + command_give_token + \
command_token_delimiter + """[player]""" + command_token_delimiter + """[token]`
Transfer a token (specified by [token]) from one of your wallets to another player's (specified by \
[player]) main wallet. [token] can be either the name or the hash.
"""
info_give_towallet = """
Syntax: `""" + command_character + command_give + command_token_delimiter + command_give_towallet \
+ command_token_delimiter + """[wallet]""" + command_token_delimiter + """[amount]`
Transfer an amount of coins (specified by [amount]) from one of your wallets to another wallet \
(specified by [wallet])
"""
info_give_wallet = """
Syntax: `""" + command_character + command_give + command_token_delimiter + command_give_wallet + \
command_token_delimiter + """[player]""" + command_token_delimiter + """[wallet]`
Give another player (specified by [player]) a wallet (specified by [wallet]). [wallet] can be \
either the name or hash. Different from `""" + command_character + command_wallet + \
command_token_delimiter + command_wallet_give + """` only in order of arguments.
"""
info_ls = """
List of commands:
\u21D2 `""" + command_character + command_about + """`
\u21D2 `""" + command_character + command_account + """`:
 \u2192 `""" + command_character + command_account + command_token_delimiter + command_account_ls \
+ command_token_delimiter + """[player]`
 \u2192 `""" + command_character + command_account + command_token_delimiter + command_account_top \
 + """`
\u21D2 `""" + command_character + command_auction + """`
\u21D2 `""" + command_character + command_bank + """`
\u21D2 `""" + command_character + command_fortune + """`
 \u2192 `""" + command_character + command_fortune + command_token_delimiter + command_fortune_cat \
+ """`
 \u2192 `""" + command_character + command_fortune + command_token_delimiter + \
command_fortune_color + """`
 \u2192 `""" + command_character + command_fortune + command_token_delimiter + \
command_fortune_wiki + """`
\u21D2 `""" + command_character + command_give + """`
 \u2192 `""" + command_character + command_give + command_token_delimiter + command_give_coin + \
 command_token_delimiter + """[player]""" + command_token_delimiter + """[amount]`
 \u2192 `""" + command_character + command_give + command_token_delimiter + command_give_token + \
 command_token_delimiter + """[player]""" + command_token_delimiter + """[token]`
 \u2192 `""" + command_character + command_give + command_token_delimiter + command_give_towallet \
 + command_token_delimiter + """[wallet]""" + command_token_delimiter + """[amount]`
 \u2192 `""" + command_character + command_give + command_token_delimiter + command_give_wallet + \
 command_token_delimiter + """[player]""" + command_token_delimiter + """[wallet]`
\u21D2 `""" + command_character + command_help + """`
\u21D2 `""" + command_character + command_info + """`
\u21D2 `""" + command_character + command_ls + """`
\u21D2 `""" + command_character + command_token + """`
 \u2192 `""" + command_character + command_token + command_token_delimiter + command_token_buy + \
 command_token_delimiter + """[token]`
 \u2192 `""" + command_character + command_token + command_token_delimiter + command_token_ls + \
 command_token_delimiter + """[token]`
 \u2192 `""" + command_character + command_token + command_token_delimiter + command_token_mint + \
 """ [name]`
 \u2192 `""" + command_character + command_token + command_token_delimiter + command_token_sell + \
 command_token_delimiter + """[token]""" + command_token_delimiter + """[cost]`
 \u2192 `""" + command_character + command_token + command_token_delimiter + command_token_unown + \
 command_token_delimiter + """[token]`
 \u2192 `""" + command_character + command_token + command_token_delimiter + command_token_unsell \
 + command_token_delimiter + """[token]`
\u21D2 `""" + command_character + command_wallet + """`
 \u2192 `""" + command_character + command_wallet + command_token_delimiter + \
 command_wallet_destroy + command_token_delimiter + """[wallet]`
 \u2192 `""" + command_character + command_wallet + command_token_delimiter + command_wallet_give \
 + command_token_delimiter + """[wallet]""" + command_token_delimiter + """[player]`
 \u2192 `""" + command_character + command_wallet + command_token_delimiter + command_wallet_init \
 + command_token_delimiter + """[name]`
 \u2192 `""" + command_character + command_wallet + command_token_delimiter + command_wallet_ls + \
 command_token_delimiter + """[wallet]`
 \u2192 `""" + command_character + command_wallet + command_token_delimiter + command_wallet_main \
 + command_token_delimiter + """[wallet]`
 \u2192 `""" + command_character + command_wallet + command_token_delimiter + command_wallet_move \
 + command_token_delimiter + """[wallet]""" + command_token_delimiter + """[target]""" + \
 command_token_delimiter + """[amount]`
 \u2192 `""" + command_character + command_wallet + command_token_delimiter + command_wallet_movet \
 + command_token_delimiter + """[wallet]""" + command_token_delimiter + """[target]""" + \
 command_token_delimiter + """[token]`
"""
info_none = """
Sorry, but the command `%s` wasn't recognized. See if you have any typos, or are thinking of a \
subcommand for another command (i.e. `init` isn't a command, but `wallet init` is). Or maybe there \
isn't documentation for that yet. If you think there should be, tell the administrator.
"""
info_token = """
The `""" + command_token + """` commands are all related to the buying, selling and distribution \
of tokens. When you use tokens that you own, you can refer to the tokens by their name. Otherwise, \
refer to them by their hash. Token commands:
- `""" + command_token + command_token_delimiter + command_token_buy + """`
- `""" + command_token + command_token_delimiter + command_token_ls + """`
- `""" + command_token + command_token_delimiter + command_token_mint + """`
- `""" + command_token + command_token_delimiter + command_token_sell + """`
- `""" + command_token + command_token_delimiter + command_token_unown + """`
- `""" + command_token + command_token_delimiter + command_token_unsell + """`
"""
info_token_buy = """
Syntax: `""" + command_character + command_token + command_token_delimiter + command_token_buy + \
command_token_delimiter + """[token]`
The [token] has to be the hash of a token at auction because if you owned it, then you wouldn't be \
buying it. If the owner of the token has listed it for auction with `""" + command_character + \
command_token + command_token_delimiter + command_token_sell + """`, then they had to have \
specified a price, possibly """ + symbol + """0. If the caller of the command has a wallet with \
that many coin the token will be transferred to their main wallet.
"""
info_token_list = """
Syntax: `""" + command_character + command_token + command_token_delimiter + command_token_ls + \
command_token_delimiter + """[token]`
The [token] is either the hash of any token or the name of a token owned by the caller of this \
command. This command just gives information about the token.
"""
info_token_mint = """
Syntax: `""" + command_character + command_token + command_token_delimiter + command_token_mint + \
""" [name]`
After uploading an image or in the same message as an image upload, you can use the `""" + \
command_token_mint + """` command to turn it into a token with the specified [name]. This does NOT \
mean that you own the token. Instead, it is given to the bank and is auctioned for """ + symbol + \
"""0. Anyone can buy it, including the creator. You do get an amount of coin equal to the amount \
of coins in the bank divided by """ + str(return_diminish_factor) + """, rounded up; if you have a \
wallet. If you do not have any wallets, you can still mint tokens and you will still be listed as \
the creator, but you do not get the payout from the bank. If you successfully mint a token, a \
message will appear with the token which lists the hash, if you choose to buy the token you just \
minted.
"""
info_token_sell = """
Syntax: `""" + command_character + command_token + command_token_delimiter + command_token_sell + \
command_token_delimiter + """[token]""" + command_token_delimiter + """[cost]`
The [token] can be either the hash or name of a token. This command lists the token for auction, \
and changes the cost (specified by [cost]). It does not automatically sell the token, because \
there has to be a buyer. You can make the token cost as much as you like, but there are only """ + \
symbol + str(default_cryptosystem_size) + """ in existence, so much more than that is not \
recommended. If you go back on your decision to list a token for auction (before it is sold), use \
`""" + command_character + command_token + command_token_delimiter + command_token_unsell + """`.
"""
info_token_unown = """
Syntax: `""" + command_character + command_token + command_token_delimiter + command_token_unown + \
command_token_delimiter + """[token]`
It's happened to all of us. We accidentally spend \u039E150 on an image of a monkey that was \
procedurally generated, and all of your friends are talking about how stupid you would have to be \
to do that. Don't worry. You can get rid of all of the evidence by using this command. The [token] \
can be either the hash or name of a token. After using this command, the token will go back to the \
bank and will be put up for auction so someone else can make the same mistake you did. (You don't \
get your coins back though, you only get your honor back.)
"""
info_token_unsell = """
Syntax: `""" + command_character + command_token + command_token_delimiter + command_token_unsell \
+ command_token_delimiter + """[token]`
The [token] can be either the hash or name of a token. If you decided you don't want to sell a \
token, using this command will remove it from auction, and then you can relist it later, or not, \
or give it to someone idk.
"""
info_wallet = """
The `""" + command_wallet + """` commands are all related to creating, using, sharing, and \
destruction of wallets. When you use wallets that you own, you can refer to the wallets by their \
name. Otherwise, refer to them by their hash. Wallet commands:
- `""" + command_wallet + command_token_delimiter + command_wallet_destroy + """`
- `""" + command_wallet + command_token_delimiter + command_wallet_give + """`
- `""" + command_wallet + command_token_delimiter + command_wallet_init + """`
- `""" + command_wallet + command_token_delimiter + command_wallet_ls + """`
- `""" + command_wallet + command_token_delimiter + command_wallet_main + """`
- `""" + command_wallet + command_token_delimiter + command_wallet_move + """`
- `""" + command_wallet + command_token_delimiter + command_wallet_movet + """`
"""
info_wallet_destroy = """
Syntax: `""" + command_character + command_wallet + command_token_delimiter + \
command_wallet_destroy + command_token_delimiter + """[wallet]`
If you have more than 1 wallet, you can move all of the coins and tokens in a wallet (specified by \
[wallet]) to your main wallet. If [wallet] is your main wallet, coins and tokens are moved to your \
new main wallet. Then [wallet] is destroyed.
"""
info_wallet_give = """
Syntax: `""" + command_character + command_wallet + command_token_delimiter + command_wallet_give \
+ command_token_delimiter + """[wallet]""" + command_token_delimiter + """[player]`
Give another player (specified by [player]) a wallet (specified by [wallet]). [wallet] can be \
either the name or hash. Different from `""" + command_character + command_give + \
command_token_delimiter + command_give_wallet + """` only in order of arguments."""
info_wallet_init = """
Syntax: `""" + command_character + command_wallet + command_token_delimiter + command_wallet_init \
+ command_token_delimiter + """[name]`
Initializes a new wallet with the name [name]. If this works, a message will be returned that has \
the seed for a new wallet, and the sha256 hash. Wallets and tokens both have hashes that allow \
them to be uniquely identified. Names, on the other hand, are useful for identification, but are \
not unique.
The seed is generated by the creator of the wallet, the name given to the wallet at creation, and \
the Unix timestamp. The final field is the stamp, which is just eight randomly generally digits. \
This prevents someone from accidentally creating two wallets in the same second with the same name \
which would have the same hash.
"""
info_wallet_ls = """
Syntax: `""" + command_character + command_wallet + command_token_delimiter + command_wallet_ls + \
command_token_delimiter + """[wallet]`
The [wallet] is either the hash of any wallet or the name of a wallet owned by the caller of this \
command. This command just gives information about the wallet.
"""
info_wallet_main = """
Syntax: `""" + command_character + command_wallet + command_token_delimiter + command_wallet_main \
+ command_token_delimiter + """[wallet]`
Designates a wallet (specified by [wallet]) as your main wallet. If other users want to give you \
coins or tokens, they will go into your main wallet. (Unless that person specifically deposits \
coins into a wallet with `""" + command_character + command_give + command_token_delimiter + \
command_give_towallet + """`.)
"""
info_wallet_move = """
Syntax: `""" + command_character + command_wallet + command_token_delimiter + command_wallet_move \
+ command_token_delimiter + """[wallet]""" + command_token_delimiter + """[target]""" + \
command_token_delimiter + """[amount]`
Move an amount of coins (specified by [amount]) from a wallet (specified by [wallet]) to another \
wallet (specified by [target]). [wallet] is a wallet owned by the caller of the function, and can \
be either a name or a hash. [target] has to be a hash.
"""
info_wallet_movet = """
Syntax: `""" + command_character + command_wallet + command_token_delimiter + command_wallet_movet \
+ command_token_delimiter + """[wallet]""" + command_token_delimiter + """[target]""" + \
command_token_delimiter + """[token]`
Move a token (specified by [token]) from a wallet (specified by [wallet]) to another wallet \
(specified by [target]). [wallet] is a wallet owned by the caller of the function, and can be \
either a name or a hash. [target] has to be a hash. [token] can be either a name or a hash.
"""

perm_ru = 0 # Permissions - Regular User
perm_su = 1 # Permissions - Super User

status_name = command_character + command_info

text_account_info = """
Created wallets: %s
Wallets: %s
Coins in wallets: %s\n
**Wallets and Tokens:**%s
"""
text_account_title = "Account information for %s:"
text_account_top = "Gave contents of '%saccount top' to %s"
text_auction = "Gave contents of '%sauction' to %s"
text_auction_none = "It looks like no one wants to auction tokens right now :("
text_command_infoprompt = "Maybe try `" + command_character + command_info + " %s`"
text_command_parseerror = "Error parsing `%s`."
text_command_unknown = "Unknown command `%s`"
text_fortune = "Gave fortune '%s' to %s."
text_fortune_color = "Gave color '%s' to %s"
text_fortune_wiki = "Gave wiki '%s' to %s"
text_give_coin = "Successfully gave %s%s to %s"
text_give_token = "Successfully gave %s to %s"
text_give_towallet = "Successfully gave %s%s to wallet %s"
text_loaded_cryptosystem = "Loaded cryptosystem"
text_loaded_player = "Loaded in %s"
text_loaded_token = "Loaded in %s"
text_loaded_wallet = "Loaded in %s"
text_local_command_thread = "Started local command thread"
text_log_message = "%s"
text_log_time = "%s[%s]%s "
text_logged_in = "Logged in as %s!"
text_new_cryptosystem = "Creating new cryptosystem"
text_new_player = "Welcoming %s! (New player)"
text_new_token = "Creating token %s with sha256 hash %s"
text_new_wallet = "Creating wallet %s with sha256 hash %s"
text_reserve = "Reserve: " + symbol + "%s. Bank: " + symbol + "%s"
text_reserve_reserve = "Reserved " + symbol + "%s. " + text_reserve
text_reserve_unreserve = "Unreserved " + symbol + "%s to %s. " + text_reserve
text_running_bot = "Running bot..."
text_save = "Saved cryptosystem"
text_target_token_not_found = "Couldn't find %s."
text_target_user_not_found = "Couldn't find %s."
text_target_wallet_not_found = "Couldn't find a target wallet"
text_target_wallet_not_found_w_user = "Couldn't find a target wallet (requested by %s)"
text_template_account = "**Players:**%s\n\n**Wallets:**%s\n\n**Tokens:**%s"
text_template_player = "\n%s \u2015 `%s (%s%s net worth)`"
text_template_token = "\n%s \u2015 `%s (valued at %s%s)\n%s`"
text_template_sub_token = "\n\u2015 %s `%s (valued at %s%s)\n%s`"
text_template_wallet = "\n%s \u2015 `%s (with %s%s) owned by %s\n%s`"
text_token_attachment_unknown = "Couldn't find an attachment to mint in recent channel history."
text_token_body = """
Created by %s at %s.
Currently valued at %s%s.
"""
text_token_buy = "Successfully bought %s"
text_token_footer = "Seed and sha256 hash: %s %s"
text_token_mint_warning = "Successfully minted token, but could not give payout because no wallet could be found."
text_token_not_found = "Couldn't find token %s"
text_token_not_in_auction = "%s isn't at auction."
text_token_sell = "Successfully listed %s."
text_token_title = "**%s** : *%s*"
text_token_unown = "Successfully unowned %s. (Is that a verb?)"
text_token_unsell = "Successfully unlisted %s."
text_top_accounts = "Top Accounts"
text_wallet_already_exists = "%s, you already have a wallet named '%s'"
text_wallet_body = """
Created by %s at %s.
Currently has %s%s.

**Tokens:**"""
text_wallet_destroy = "Successfully destroyed wallet."
text_wallet_destroy_error = "You don't have enough wallets to destroy wallets."
text_wallet_footer = "Seed and sha256 hash: %s %s"
text_wallet_give = "Successfully gave %s to %s."
text_wallet_mained = "Made '%s' %s's main wallet."
text_wallet_move = "Successfully moved %s%s to %s."
text_wallet_move_error = "Couldn't find %s."
text_wallet_movet = "Moved %s to %s."
text_wallet_not_found = "Couldn't find a wallet with %s coins..."
text_wallet_not_found_generic = "Couldn't find %s"
text_wallet_not_found_w_user = "Couldn't find a wallet with %s coins (requested by %s)"
text_wallet_title = "**%s** : *%s*"
text_warning = "%s(Warning)%s %s"
