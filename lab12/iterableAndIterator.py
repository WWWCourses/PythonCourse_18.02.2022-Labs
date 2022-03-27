# l = [1,2,3]

# # l_iter = l.__iter__()
# l_iter = iter(l)

# print( next(l_iter) )
# print( l_iter.__next__() )
# print( next(l_iter) )
# # print( next(l_iter) )

# for el in l:
# 	print(el)

# d = {
# 	1:'foo',
# 	2:'bar'
# }

# d_iter = iter(d)
# print( next(d_iter) )


# for el in range(1,5):
# 	print(el)

# # import itertools
# from itertools import count,cycle

# # for el in count(1):
# # 	if el==10: break

# # 	print(el)


# tries = 10
# for el in cycle([1,2,3]):
# 	if tries==0: break

# 	print(el,end=' ')
# 	tries -= 1


# -------------------------- create custom iterable -------------------------- #

# 1,1,2,3,5,8,...
class Fibonachi:
	def __init__(self, max):
		self.prev = 0
		self.next = 1
		self.max =  max

	def __iter__(self):
		return self

	def __next__(self):
		if self.max == 0:
			raise StopIteration
		self.max -= 1

		value = self.prev + self.next
		self.prev = self.next
		self.next = value

		return value

fib = Fibonachi(10)
# print( next(fib) )
# print( next(fib) )
# print( next(fib) )
# print( next(fib) )
# print( next(fib) )
# print( next(fib) )
# print( next(fib) )
# print( next(fib) )

for el in fib:
	print(el)