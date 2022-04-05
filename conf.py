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
return_diminish_factor = 30
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
command_info = "info"
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
	"<PC Load Letter>",
	"2 + 2 = 5",
	"254ebc9d57cb06da5ea1bf685c7a04b0bfe9c808d5dcb5d093fc640f713dab9e",
	"dQw4w9WgXcQ",
	"Epstein didn't kill himself.",
	"Everybody walk the dinosaur",
	"Go Greendale!",
	"Hey you, you're finally awake",
	"HEYYEYAAEYAAAEYAEYAA",
	"https://en.wikipedia.org/wiki/Wikipedia",
	"https://twitter.com",
	"Insane (in the Brain)",
	"Loading: 142%",
	"Not PS5 Compatible ... yet",
	"Open the door, get on the floor",
	"Or is it?",
	"Police police police police.",
	"Return to Monke",
	"Sponsored by Duolingo - \"Have you done your Spanish?\"",
	"Sponsored by Hooli",
	"This message will never appear on the splash screen, isn't that weird?",
	"What do you know about rolling down in the deep?",
	"while (true) return (true) ?: true;"
]

info_about = """
Willcoin is a discord cryptosystem. Users can create any (realistic) number of wallets and they \
can assign coins to each one, as well as move tokens betwenn wallets, which are like peices of \
digital artwork. Users can get coins by minting tokens or trading coins.

Willcoin is open-source. The GitHub page is here: https://github.com/will-koz/willcoin
"""
info_account = """TODO info account"""
info_account_list = """TODO info account list"""
info_account_top = """TODO account top"""
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
info_general = """TODO info general"""
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
info_give_coin = """TODO give coin"""
info_give_token = """TODO give token"""
info_give_towallet = """TODO give towallet"""
info_give_wallet = """TODO give wallet"""
info_ls = """TODO ls"""
info_none = """
Sorry, but the command `%s` wasn't recognized. See if you have any typos, or are thinking of a \
subcommand for another command (i.e. `init` isn't a command, but `wallet init` is). Or maybe there \
isn't documentation for that yet. If you think there should be, tell the administrator.
"""
info_token = """
The `token` commands are all related to the buying, selling and distribution of tokens. When you \
use tokens that you own, you can refer to the tokens by their name. Otherwise, refer to them by \
their hash. Token commands:
- `""" + command_token + command_token_delimiter + command_token_buy + """`
- `""" + command_token + command_token_delimiter + command_token_ls + """`
- `""" + command_token + command_token_delimiter + command_token_mint + """`
- `""" + command_token + command_token_delimiter + command_token_sell + """`
- `""" + command_token + command_token_delimiter + command_token_unown + """`
- `""" + command_token + command_token_delimiter + command_token_unsell + """`
"""
info_token_buy = """TODO token buy"""
info_token_list = """TODO token list"""
info_token_mint = """TODO token mint"""
info_token_sell = """TODO token sell"""
info_token_unown = """TODO token unown"""
info_token_unsell = """TODO token unsell"""
info_wallet = """TODO wallet"""
info_wallet_destroy = """TODO wallet destory"""
info_wallet_give = """TODO wallet give"""
info_wallet_init = """TODO wallet init"""
info_wallet_ls = """TODO wallet ls"""
info_wallet_main = """TODO wallet main"""
info_wallet_move = """TODO wallet move"""
info_wallet_movet = """TODO wallet movet"""

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
