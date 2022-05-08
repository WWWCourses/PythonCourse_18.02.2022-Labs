
# 2. Дефинирайте клас Shape със само един метод calculateSurface() и полета width и
# height. Дефинирайте два нови класа за триъгълник и правоъгълник, които
# имплементират споменатият метод. Този метод трябва да връща площта на
# правоъгълника (height*width) и триъгълника (height*width/2). Дефинирайте клас за
# кръг с подходящ конструктор, при когото при инициализация и двете полета (height и
# width) са с еднаква стойност (радиуса), и имплементирайте метод за изчисляване на
# площта. Направете списък от различни фигури и сметнете площта на всичките в друг
# списък.
# Вход:
# На първия ред ще се намира цяло число броя на фигурите които трябва да бъдат
# прочетени. Първата дума ще обозначава вида на фигурата ( „Circle“, „Triangle“ и
# “Rectangle” ). Ако фигурата е кръг след това добавяме едно дробно число показващо
# диаметъра му. Ако фигурата е триъгълник или правоъгълник ще следват две дробни
# числа – широчинат и височината му. (Всеки елемент от входа е разделен от другите
# чрез празно поле)
# Изход:
# На отделен ред да се изпише дробно число показващо площта на всяка въведена
# фигура.
#

import math

class Shape:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def calculateSurface(self, x, y):
		return self.width * self.height

class Rectangle(Shape):
	def __init__(self, width, height):
		super().__init__(width, height)

class Triangle(Shape):
	def __init__(self, width, height):
		super().__init__(width, height)

	def calculateSurface(self, x, y):
		return (self.width * self.height) / 2

class Circle:
	def __init__(self, r):
		self.r = r

	def calculateSurface(self, r):
		return math.pi * (r ** 2)


number_of_shapes = int(input("How many shapes would you like to see: "))

for i in range(number_of_shapes-1):
	shape = input('Enter a shape: ')
	if shape == 'rectangle':
		height = float(input("Please provide the height in cm: "))
		width = float(input("Please provide the width in cm: "))
		s1 = Rectangle(height,width)
		s1.calculateSurface(height, width)
	elif shape == 'triangle':
		height = float(input("Please provide the height in cm: "))
		width = float(input("Please provide the width in cm: "))
		s1 = Triangle(height,width)
		s1.calculateSurface(height, width)
	elif shape == 'circle':
		radius = float(input("Please provide the radius in cm: "))
		shape = Circle
		Circle.calculateSurface(radius)


