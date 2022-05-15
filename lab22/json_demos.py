import json

# books = [
# 	['To Kill a Mockingbird','Harper Lee',1960],
# 	['Book 2', 'Author 2', 2000]
# ]

books = [
	{
		'book':'To Kill a Mockingbird',
		'author':{
			'name':'Harper Lee',
			'country':'USA'
		},
		'year':1960
	},
	{
		'book':'Book2',
		'author':{
			'name':'Author 2',
			'country':'UK'
		},
		'year':2000
	},
]

def save_data(filename,data):
	with open(filename,'w') as f:
		json.dump(data,f)

def load_books(filename):
	with open(filename,'r') as f:
		books = json.load(f)

	return books;

save_data('./books.json',books)

books = load_books('./books.json')
print(books)
