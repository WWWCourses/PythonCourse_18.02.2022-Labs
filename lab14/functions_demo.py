# def get_user_data():
# 	user_age = int(input("Enter your age: "))
# 	user_name = input("Enter your name: ")


# def validate_user_data():
# 	pass


# def greet_user(user_name):
# 	print('~' * 50)
# 	print(f'Hello {user_name}!')
# 	print('~' * 50)


# greet_user('Ada')
# greet_user('Pesho')
# greet_user('Maria')


# def add(a,b,c):
# 	print(a+b+c)

# add(2,3) # 5
# add(3,4) # 7


# def do_something_with_user(user_data):
# 	print(f"Hi {user_data['name']}, you are {user_data['age']} years old.")

	# user_data['age'] += 1

# ada = {
# 	'name': 'Ada',
# 	'age': 25
# }

# pesho = {
# 	'name': 'Pesho',
# 	'age': 32
# }

# do_something_with_user({
# 	'name': 'Maria',
# 	'age': 45
# })

# do_something_with_user(pesho)
# do_something_with_user(ada)

# --------------------------- positional arguments --------------------------- #
# def foo(x=3,y=99):
# 	# x = 1, y = 2
# 	print(x,y)

# foo(1,2)


# ----------------------------- keyword arguments ---------------------------- #
# def foo(x,y,user_name, user_age):
# 	print(user_age)

# foo(1,2, user_age=45, user_name='Maria')

# ----------------------------------- *args ---------------------------------- #
# def foo(x,y,*args):
# 	# x = 1, y = 2, args = (3,4,5)
# 	print(args)

# foo(1,2,3,4,5)

# def add(*alabala):
# 	print(sum(alabala))

# add(2,3) # 5
# add(2,3,4) # 9
# add(2,3,4,5) # 14

# --------------------------------- **kwargs --------------------------------- #
# def foo(**kw):
# 	print(kw)

# foo(y=1,x=3)
# foo(y=1,x=3,z=2)

# pure functions
# def foo(x,y):
# 	if x>0:
# 		return x + y
# 	else:
# 		return x - y



# res = foo(3,4) + foo(-4,5)
# print(res)

# print( 2+2 )

# print( foo(3,4) )

def foo(x,y):
	print(x,y)
	return 2

res = foo(1,2)
print(res)
















