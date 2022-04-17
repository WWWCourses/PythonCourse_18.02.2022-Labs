class Car:
	# class attributes:
	count = 0

	### instance methods
	def __init__(self,color, speed):
		Car.count_cars()

		# instance attributes
		self.color = color
		self.speed = speed

	def drive(self):
	 	print(f'The {self.color} car is driving with {self.speed} km.h')

	# utility function (Static Method)
	def count_cars():
		Car.count +=1

	# class method
	@classmethod
	def foo(cls):
		print(cls)


ford = Car('red', 200)
bmw = Car('black', 300)

Car.foo()
ford.foo()




print(f'{Car.count} are created!')
ford.drive()  # drive(ford)








