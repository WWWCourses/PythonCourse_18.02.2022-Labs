# endless loop
# while True:
# 	print('hi')

# while False:
# 	print('hi')


# i = 1
# while i<=5:
# 	print(i)
# 	i+=1

# the same as above
# for i in range(1,6):
# 	print(i)


# for i in range(50):
# 	user_age = input('Enter your age:')
# 	if user_age.isnumeric():
# 		user_age = int(user_age)
# 		break



# while-do loop
# user_age = input('enter your age:')
# while not user_age.isnumeric():
# 	user_age = input('enter your age:')

# do-while loop:
# do {
# 	user_age = input('enter your age:')
# } while not user_age.isnumeric()

# while True:
# 	user_age = input('enter your age:')
# 	if user_age.isnumeric():
# 		user_age = int(user_age)
# 		break

# ---------------------------- nested while loops ---------------------------- #

i = 0
while i<3:
	print(i)
	j = 0
	while j<3:
		print(20*'*', j)
		j+=1

	i+=1

