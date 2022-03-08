# for i in range(10):
# 	print(i)


# ----------------------------------- range ---------------------------------- #
# range(5)   		# 0,1,2,3,4
# range(0,5) 		# 0,1,2,3,4
# range(0,5,1) 		# 0,1,2,3,4
# range(0,5,2)	# 0,2,4

# for i in range(5):
# 	print(i)

# for i in range(0,5):
# 	print(i)

# for i in range(0,5,2):
# 	print(i)

# for i in range(-1, -5, -3):
# 	print(i)

# ------------------------------- for in string ------------------------------ #
# str1 = 'abcdef'
# for l in str1:
# 	for i in range(5):
# 		print(l,i)


# l = a
# i = 0
# i = 1
# ...
# i = 4

# l = b
# i = 0
# i = 1
# ...
# i = 4

# --------------------------------- continue --------------------------------- #
# print numbers 1..10, without numbers which are divisible by 3
# for num in range(1,11):
# 	if num%3 == 0:
# 		continue

# 	print(num)

# print numbers 1..10, without numbers which are divisible by 3 or by 5
# for num in range(1,21):
# 	if num%3 == 0 or num%5==0:
# 		continue

# 	print(num)

# ----------------------------------- break ---------------------------------- #
# for num in range(2,10,2):
# 	if num==4:
# 		break

# 	print(num)

# print('END')


# for i in range(5):
# 	for j in range(3):
# 		if i == 2:
# 			break
# 		print(f'j = {j}')

# 	print(f'i = {i}')


# i = 0
	# j = 0
	# j = 1
	# j = 2
	# i = 0
# i = 1
	# j = 0
	# j = 1
	# j = 2
	# i = 1
# i = 2
	# j = 0,1,2
	# 0,1,2,3


# ------------------------------- pass in loop ------------------------------- #
# print('START')

# for i in range(20_000_000):
# 	i**2

# print('END')


