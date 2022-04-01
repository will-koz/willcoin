administration = "Admin"
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

command_account = "account"
command_account_ls = "ls"
command_account_top = "top"
command_auction = "auction"
command_exit = "exit"
command_fortune = "fortune"
command_fortune_cat = "cat"
command_fortune_color = "color"
command_fortune_wiki = "wiki"
command_give = "give"
command_give_wallet = "wallet"
command_info = "info"
command_reserve = "reserve"
command_save = "save"
command_token = "token"
command_token_buy = "buy"
command_token_ls = "ls"
command_token_mint = "mint"
command_token_sell = "sell"
command_token_unown = "unown"
command_token_unsell = "unsell"
command_unreserve = "unreserve"
command_wallet = "wallet"
command_wallet_destroy = "destroy"
command_wallet_give = "give"
command_wallet_init = "init"
command_wallet_ls = "ls"
command_wallet_main = "main"
command_wallet_move = "move"
command_wallet_movet = "movet"

fortunes = [
	":(){:|:&};:",
	"\\*\\*Sample Fortune\\*\\*",
	"\u0D9E",
	"\u221E\u00B2 - 1 = (\u221E - 1)(\u221E + 1)",
	"2 + 2 = 5",
	"254ebc9d57cb06da5ea1bf685c7a04b0bfe9c808d5dcb5d093fc640f713dab9e",
	"Epstein didn't kill himself.",
	"https://en.wikipedia.org/wiki/Wikipedia",
	"https://twitter.com",
	"Police police police police.",
	"Sponsored by Hooli",
	"This message will never appear on the splash screen, isn't that weird?",
	"What do you know about rolling down in the deep?",
	"while (true) return (true) ?: true;"
]

info_about = """
TODO
"""
info_fortune = """
The fortune comand is used to get random content. It can be used to get a random unix fortune-like
fortune. It will be able to get a random cat image, wikipedia page, and meme soon. TODO
"""
info_none = """
Sorry, but the command '%s' wasn't recognized. See if you have any typos, or are thinking of a
subcommand for another command (i.e. 'init' isn't a command, but 'wallet init' is). Or maybe there
isn't documentation for that yet. If you think there should be, tell the administrator.
"""
info_token = """
TODO
"""

perm_ru = 0 # Permissions - Regular User
perm_su = 1 # Permissions - Super User

text_account_info = """
Created wallets: %s
Wallets: %s
Coins in wallets: %s
"""
text_account_title = "Account information for %s:"
text_auction_none = "It looks like no one wants to auction tokens right now :("
text_command_infoprompt = "Maybe try `" + command_character + command_info + " %s`"
text_command_parseerror = "Error parsing '%s'."
text_command_unknown = "Unknown command '%s'"
text_fortune = "Gave fortune '%s' to %s."
text_fortune_color = "Gave color '%s' to %s"
text_log_message = "%s"
text_log_time = "%s[%s]%s "
text_logged_in = "Logged in as %s!"
text_new_player = "%s is doing something that might require player initialization"
text_new_token = "Creating token %s with sha256 hash %s"
text_new_wallet = "Creating wallet %s with sha256 hash %s"
text_reserve = "Reserve: " + symbol + "%s. Bank: " + symbol + "%s"
text_reserve_reserve = "Reserved " + symbol + "%s. " + text_reserve
text_reserve_unreserve = "Unreserved " + symbol + "%s. " + text_reserve
text_target_user_not_found = "Couldn't find %s."
text_template_account = "**Players:**%s\n\n**Wallets:**%s\n\n**Tokens:**%s"
text_template_player = "\n%s \u2015 `%s (%s%s net worth)`"
text_template_token = "\n%s \u2015 `%s (valued at %s%s)\n%s`"
text_template_wallet = "\n%s \u2015 `%s (with %s%s)\n%s`"
text_token_body = """
Created by %s at %s.
Currently valued at %s%s.
"""
text_token_footer = "Seed and sha256 hash: %s %s"
text_token_title = "**%s** : *%s*"
text_top_accounts = "Top Accounts"
text_wallet_already_exists = "%s, you already have a wallet named '%s'"
text_wallet_body = """
Created by %s at %s.
Currently has %s%s.
"""
text_wallet_footer = "Seed and sha256 hash: %s %s"
text_wallet_mained = "Made '%s' %s's main wallet."
text_wallet_title = "**%s** : *%s*"
text_warning = "%s(Warning)%s %s"
