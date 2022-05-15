# -------------------------------- Задача 4-1 -------------------------------- #
# class A:
# 	def __init__(self, x=1):
# 		print('A constructor')
# 		self.x = x

# class B(A):
# 	def __init__(self, y=1):
# 		super().__init__(20)
# 		# equivalent to above
# 		# A.__init__(self,20)

# 		self.y = y

# def main():
# 	obj = B(10) # B.__init__(obj,10)
# 	print(obj.x, obj.y)

# main()


# -------------------------------- Задача 5-1 -------------------------------- #
# class Tmp:
# 	def test(self):
# 		print('test of Tmp called')

# class A:
# 	def test(self):
# 		print('test of A called')

# class B(A,Tmp):
# 	def test(self):
# 		print('test of B called')
# 		super().test()
# 		# A.test(self)
# 		# Tmp.test(self)

# class C(A):
# 	def test(self):
# 		print('test of C called')
# 		super().test()

# class D(B,C):
# 	def test2(self):
# 		print('test of D called')

# d = D()
# d.test()
# Python's MRO (Method Resolution Order)
#https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/
# Class D -> Class B -> Class C -> Class A

#'test of B called'
#'test of C called'
#'test of A called'

# -------------------------------- Задача 5-2 -------------------------------- #
class A:
	def __init__(self): # self = b
		self.multiply(15)
		print(self.i)

	def multiply(self,i):
		self.i = 4*i

class B(A):
	def __init__(self):
		super().__init__()

	def multiply(self,i): # self = b, i = 15
		self.i = 2*i

b = B()

# A) 15 B)30 C) 45 D) 60 E) Error