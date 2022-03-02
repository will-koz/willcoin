class Wallet:
	def __init__ (self, creator = "Anon", name = "NewWallet"):
		seed_prefix = creator + "-" + name
		seed_suffix = 0
		print("Seed is " + seed_prefix + str(seed_suffix))

class Cryptosystem:
	total_willcoin = 0
	bank = Wallet(creator = "SystemWill", name = "BankOfWill")
	def __init__ (self, location = None, size = 1000):
		self.new_cryptosystem(size)

	def new_cryptosystem (self, size = 1000):
		total_willcoin = size
