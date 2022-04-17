class Predator:
	def __init__(self,  name, food) -> None:
		self.name = name
		self.food=food

	def eat(self):
		print(f'{self.name} is eating {self.food}!')

class Dog(Predator):
	def __init__(self, name, food, chip_id) -> None:
		self.chip_id = chip_id
		# Predator.__init__(self, name,food) # not good
		super().__init__(name,food) # good

	def eat(self):
		print(f'{self.chip_id} is eating')
		super().eat()

class Cat(Predator):
	def __init__(self, name, food) -> None:
		super().__init__(name,food) # good


sharo = Dog('Sharo', 'meat', 234432432)
tom = Cat('Tom', 'fish')

sharo.eat()
tom.eat()
