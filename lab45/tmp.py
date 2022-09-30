class Base:
	def __init__(self,x) -> None:
		self.x = x

	def print_x(self):
		print(self.x)

class Child(Base):
	def __init__(self, x) -> None:
		super().__init__(x)


a = Child(1)
a.print_x()