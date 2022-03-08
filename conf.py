administration = "Admin"
anonymous = "Anon"
bank_name = "BankOfWill"
byte_encoding = "utf-8"
command_character = '>'
command_token_delimiter = ' '
default_cryptosystem_size = 2 ** 25
default_stamp_size = 8
default_token_name = "NewToken"
default_wallet_name = "NewWallet"
request_not_found_code = 429
stamp_values = "0123456789abcdef"

ansi_escape = "\033["
ansi_reset = ansi_escape + "0m"
ansi_dull = ansi_escape + "2m"
ansi_error = ansi_escape + "1;31m"

command_exit = "exit"
command_fortune = "fortune"

fortunes = [
	"**Sample Fortune**",
	"2 + 2 = 5"
]

perm_ru = 0 # Permissions - Regular User
perm_su = 1 # Permissions - Super User

text_command_unknown = "Unknown command '%s'"
text_new_token = "Creating token %s with sha256 hash %s"
text_new_wallet = "Creating wallet %s with sha256 hash %s"
text_warning = "%s(Warning)%s %s"
