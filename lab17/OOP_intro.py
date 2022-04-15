# ----------------------- model data with dictionaries ----------------------- #
# car1 = {
# 	'color':'black',
# 	'speed':200
# }

# car2 = {
# 	'color':'red',
# 	'speed':300
# }

# def drive_car(car):
# 	print(f'The {car["color"]} car is driving with {car["speed"]} km.h')

# -------------------------- model data with classes ------------------------- #
class Car:
	# class attributes:
	count = 0

	### methods
	# constructor (__init__):
	def __init__(self,color, speed):
		print('Car is created')
		# instance attributes
		self.color = color
		self.speed = speed


	def drive(self):
	 	print(f'The {self.color} car is driving with {self.speed} km.h')



# create objects (instances):

car1 = Car('black', 200)
car2 = Car('red', 300)

car1.drive()
car2.drive()

# print(car1.color)
# print(car2.color)
# print(Car.color)

# car1.color = 'red'

# print(car1.color)
# print(car2.color)
# print(Car.color)

