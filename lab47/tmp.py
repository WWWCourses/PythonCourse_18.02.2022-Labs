class A:
	id = 1
	def __init__(self,id) -> None:
		self.id = id

for i in range(5):
	print(i)
	a = A(i)
	a.