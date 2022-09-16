import pymongo

from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.python_course


def insert_todos():
	res = db.todos.insert_many([
		{
			"title": "Learn Python",
			"completed": True,
			"dueDate": datetime.fromisoformat("2021-07-01"),
			"priority": 1,
		},
		{
			"title": "Learn Flask",
			"description":"Learn Flask to develop quick and easy web applications with the ability to scale up.",
			"completed": True,
			"dueDate": datetime.fromisoformat("2022-01-12"),
			"priority": 2
		},
		{
			"title": "Learn MongoDB",
			"completed": False,
			"dueDate": datetime.fromisoformat("2022-01-12"),
			"priority": 1
		},
		{
			"title": "Learn PyQT",
			"completed": False,
			"dueDate": datetime.fromisoformat("2021-12-01"),
			"priority": 2
		}
	])

	print(res.inserted_ids)

def read_todos():
	docs = db.todos.find()

	# docs = db.todos.find({"priority": 2}, {"_id":0,"title":1})

	# docs = db.todos.find(
	# 	{
	# 		"$and":[
	# 			{"priority": {"$gt":1}},
	# 			{"completed":True}
	# 		]

	# 	},
	# 	{"_id":0,"title":1}
	# )

	# docs = db.todos.find(
	# 	{"title": {"$regex": "python","$options":"i"}}
	# )


	# print(list(doc))
	for doc in docs:
		print(doc['title'])

def update_todo():
	res = db.todos.update_one(
		{"title": {"$regex": "python","$options":"i"}},
		{"$set":{"title":"JS"}}
	)

	print(dir(res))

def delete_todo():
	res = db.todos.delete_one(
		{"title": {"$regex": "js","$options":"i"}}
	)

	print(dir(res))

def text_search():
	# create text index for title:
	db.todos.create_index([
		("title","text")
	])

	# TODO: make it search as substring
	todos = db.todos.find(
		{
			"$text": {"$search": "Mongo"},
			"diacriticSensitive":True
		}
	)

	print(list(todos))


# delete_todo()
read_todos()

text_search()

