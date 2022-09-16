import pymongo as pm

# mongodb://username:password@localhost:27017/dbname

# connect to default host and port:
# client = pm.MongoClient()

# # connect to host at given port:
# client = pm.MongoClient('localhost', 27017)

# # connect to host at given port with specified username and password:
# client = pm.MongoClient('localhost', 27017, username='username', password='password')

# # connect using connection string in MongoDB URI format:
# client = pm.MongoClient('mongodb://localhost:27017')

# connect using connection string in MongoDB URI format with specified username and password:
client = pm.MongoClient('mongodb+srv://python_courses_test:12345678abv@cluster0.6oisd7l.mongodb.net/')

# print( client.list_database_names() )

testdb = client.testdb

# print(testdb.list_collection_names())

# ---------------------------- insert document(s) ---------------------------- #
res = testdb.todos.insert_one({"title": "Learn MongoDB", "done": False})
print(res.inserted_id)

