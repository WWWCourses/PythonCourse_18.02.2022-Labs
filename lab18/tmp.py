from telnetlib import DO


class Dog:
	age = 5

	def happyBirthday(self):
		print( self.age ) # 5
		self.age= self.age + 1

sam = Dog()
sharo=Dog()

sam.happyBirthday()

print( dir(sam) )

print( sam.age )
print( sharo.age )
print( Dog.age )
