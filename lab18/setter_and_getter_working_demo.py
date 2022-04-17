# ------------------------------ with decorators ----------------------------- #
class A:
	def __init__(self, id) -> None:
		self.id = id # setter is called

	# Getter
	@property
	def id(self):
		print('Getter is called')
		return(self.__id)

	# Setter
	@id.setter
	def id(self, value):
		print('Setter is called')
		self.__id = value


a = A(1)

a.id = 2 # setter is called
print( a.id ) # getter is called

# ---------------------------- without decorators ---------------------------- #
class B:
	def __init__(self, id) -> None:
		self.set_id(id) # setter is called

	# Getter
	def get_id(self):
		print('Getter is called')
		return(self.__id)

	# Setter
	def set_id(self, value):
		print('Setter is called')
		self.__id = value


b = B(1)

b.set_id(2) # setter is called
print( b.get_id() ) # getter is called
