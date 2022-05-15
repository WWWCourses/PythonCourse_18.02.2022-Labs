
import csv

def enter_new_book():
	# book = input('book name')
	bookName = 'A Brief History Of Time'
	author = 'Stephen Hawking'
	year = 1988

	books.append([bookName,author,year])

	print(books)

def load_books_byhand(filename):
	books = list()
	with open(filename,'r') as f:
		lines = f.readlines()
		# print(lines)
		# [
		# 	'To Kill a Mockingbird|Harper Lee|1960\n', 'Book 2|Author 2|2000\n'
		# ]
		for line in lines:
			line = line.rstrip('\n')
			books.append(line.split('|'))

	return books

def save_books_byhand(filename, books):
	with open(filename,'w') as f:
		for book in books:

			row = '|'.join([str(el) for el in book])
			row+='\n'
			f.write(row)

def save_books(filename, books):
	with open(filename, 'w', newline='') as f:
		w = csv.writer(f,delimiter="|",quotechar='"')
		w.writerow(['BookTitle', 'Author','Year'])
		w.writerows(books)

def load_books(filename):
	books = list()
	with open(filename, 'r', newline='') as f:
		r = csv.reader(f,delimiter="|",quotechar='"')

		first_line = True
		for row in r:
			if not first_line:
				books.append(row)
			else:
				first_line=False

	return books


# books = [
# 	['To Kill a Mockingbird','Harper Lee',1960],
# 	['Book 2', 'Author 2', 2000]
# ]

# save_books(filename='./books.csv', books=books)
books = load_books(filename='./books.csv')
print(books)

