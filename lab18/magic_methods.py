class Car:
	def __init__(self,color, speed):
		self.color = color
		self.speed = speed

	def __str__(self):
		# print('Str is called!')
		return f'color: {self.color}\nspeed: {self.speed}'


	def __add__(self,other):
		print('add is called')
		return self.speed + other.speed


ford = Car('red', 200)
bmw = Car('black', 300)


print( ford+bmw ) # ford.__add__(bmw)

