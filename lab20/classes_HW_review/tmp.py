# class A:
# 	id = 1
# 	pass

# # a1 = A()
# # a1.id =1
# # print(a1.id)

# A.ID = 9
# print(A.ID)
# print(A.id)


# class A:
# 	def __init__(self) -> None:
# 		pass
# 	def __str__(self):
# 		return 'lalalalallalalala'

# a = A()
# # a.foo()

# print(a)

# books_list = [
# 	{
# 		"title":"Harry Potter and the Philosopher\'s Stone",
# 		"author":"J.K.Rowling",
# 		"year":1997,
# 		"isbn":1
# 	},
# 	{
# 		"title":"Harry Potter and the Philosopher\'s Stone",
# 		"author":"J.K.Rowling",
# 		"year":1997,
# 		"isbn":2
# 	},
# ]

# def remove_book(isbn):
# 	# loop over all elements and delete elements with given isbn
# 	for book in books_list:
# 		if book['isbn'] == isbn:
# 			books_list.remove(book)

# remove_book(isbn=1)
# print(books_list)


class A:
	# static method
	def foo(x):
		print(x)

A.foo(1)

a = A()
a.foo(1)