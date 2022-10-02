class Base:
	def __init__(self,*args,**kw ):
		print(args[0])
		print(kw)

class Child(Base):
	def __init__(self, *args,**kw):
		super().__init__(*args, **kw)

child1 = Child(1,2,3, password='alabala', id=1)