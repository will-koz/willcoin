administration = "Admin"
anonymous = "Anon"
bank_name = "BankOfWill"
byte_encoding = "utf-8"
command_character = '>'
command_token_delimiter = ' '
default_cryptosystem_size = 2 ** 25
default_reserve_amount = 2 ** 10
default_stamp_size = 8
default_token_name = "NewToken"
default_wallet_name = "NewWallet"
embed_delimiter = " "
file_mode = "r"
player_name_delimiter = '#'
request_not_found_code = 429
stamp_values = "0123456789abcdef"
symbol = "\u20A9"
token = "token.txt"

ansi_escape = "\033["
ansi_reset = ansi_escape + "0m"
ansi_dull = ansi_escape + "2m"
ansi_error = ansi_escape + "1;31m"

command_account = "account"
command_account_ls = "ls"
command_exit = "exit"
command_fortune = "fortune"
command_fortune_color = "color"
command_info = "info"
command_reserve = "reserve"
command_unreserve = "unreserve"
command_wallet = "wallet"
command_wallet_destroy = "destroy"
command_wallet_init = "init"

fortunes = [
	"2 + 2 = 5",
	"\\*\\*Sample Fortune\\*\\*"
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

perm_ru = 0 # Permissions - Regular User
perm_su = 1 # Permissions - Super User

text_account_info = """
Total wallet coins: %s
"""
text_account_title = "Account information for %s:"
text_command_infoprompt = "Maybe try `" + command_character + command_info + " %s`"
text_command_parseerror = "Error parsing '%s'."
text_command_unknown = "Unknown command '%s'"
text_fortune = "Gave fortune '%s' to %s."
text_fortune_color = "Gave color '%s' to %s"
text_log_message = "%s"
text_log_time = "%s[%s]%s "
text_logged_in = "Logged in as %s!"
text_new_player = "Initializing player %s"
text_new_token = "Creating token %s with sha256 hash %s"
text_new_wallet = "Creating wallet %s with sha256 hash %s"
text_reserve = "Reserve: " + symbol + "%s. Bank: " + symbol + "%s"
text_reserve_reserve = "Reserved " + symbol + "%s. " + text_reserve
text_reserve_unreserve = "Unreserved " + symbol + "%s. " + text_reserve
text_wallet_already_exists = "%s, you already have a wallet named '%s'"
text_warning = "%s(Warning)%s %s"
