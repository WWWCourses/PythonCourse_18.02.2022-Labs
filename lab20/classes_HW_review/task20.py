
# Задача 20. Нека е дадена библиотека с книги. Дефинирайте класове съответно за
# библиотека и книга. Библиотеката трябва да съдържа име и списък от книги. Книгите
# трябва да съдържат информация за заглавие, автор, издателство, година на издаване и
# ISBN-номер. В класа, който описва библиотека, добавете методи за добавяне на книга
# към библиотеката, търсене на книга по предварително зададен автор, извеждане на
# информация за дадена книга и изтриване на книга от библиотеката.
#

class Library:
	def __init__(self, name, books_list=None):
		self.name = name
		if books_list is None:
			self.books_list = []
		else:
			self.books_list = books_list

	def add_book(self, book):
		self.books_list.append(book)

	def search_book():
		searched_author = input("Please provide the name of the author you are searching for: ")
		for book in Library.books_list:
			if book[1] == searched_author:
				print(book[1])

	def remove_book(self, book):
		self.books_list.remove(book)

	def print_all_books(self):
		for book in self.books_list:
			print(book)

class Book:
	def __init__(self, title, author, publisher, publication_year, ISBN_number):
		self.title = title
		self.author = author
		self.publisher = publisher
		self.publication_year = publication_year
		self.ISBN_number = ISBN_number

	def __str__(self):
		return f'''Book title: {self.title},
		author: {self.author},
		publisher: {self.publisher},
		publication year: {self.publication_year},
		ISBN number: {self.ISBN_number}.'''


library = Library("Sofia's Library")

book1 = Book("Harry Potter and the Philosopher\'s Stone", "J.K.Rowling", "Bloomsbury", 1997, 9780747532743)
book2 = Book("Title2", "Author2", "Publisher2","1990","834835787435843")

# library.add_book(book1)
# library.add_book(book2)

# library.remove_book(isbn='834835787435843')
# library.print_all_books()

# Library.search_book()

# print(book1)

# Library.remove_bok(book1)
