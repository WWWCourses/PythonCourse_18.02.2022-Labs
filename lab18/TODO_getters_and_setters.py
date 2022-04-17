class Account:
	def __init__(self, name, balance) -> None:
		self.__name = name
		self.__balance = balance

	# setter
	# TODO: check error
	# DONE: Getter declaration MUST precede Setter declaration
	@balance.setter
	def balance(self,new_balance):
		print('Setter: Log into DB when the balance is changed...')
		self.__balance = new_balance

	# getter
	@property
	def balance(self):
		print('Geter: Log into DB when the balance is used!!!')
		return self.__balance



maria_acount = Account('Maria', 1000)
pesho_acount = Account('Pesho', 1000)

# maria_acount.set_balance(1_000_000)
# print( maria_acount.get_balance() )

maria_acount.balance = 0  # maria_acount.balance(0)
print( maria_acount.balance )

# print( maria_acount.get_balance() )



