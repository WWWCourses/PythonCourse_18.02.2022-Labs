# ---------------------------- list comprehensions --------------------------- #
# [expression for var in iterable]
# [expression for var in iterable if condition]

# l = [1,2,3,4]
### variant with loop (non comprehenssion)
# l_even = []
# for el in l:
# 	if el % 2 == 0:
# 		l_even.append(el)

### variant with comprehenssion:
# l_even = [el for el in l if el % 2 == 0]

# print(l_even)

# ---------------------------- dict comprehensions --------------------------- #
# {key:value for var in iterable}
# {key:value for var in iterable if condition}
# d = {'a':1,'b':2,'c':3}

### variant with loop (non comprehenssion)
# d_new = {}
# for key, value in d.items():
# 	d_new[key] = value ** 2

### variant with comprehenssion:
# d_new = {key:value ** 2 for key, value in d.items()}
# print(d_new)


# ------------------------- generator comprehensions ------------------------- #
# (expression for var in iterable)
# (expression for var in iterable if condition)

### with generator function
# def even_generator():
# 	for i in range(1, 10):
# 		if i % 2 == 0:
# 			print(f'i in generator: {i}')
# 			yield i
# even_gen = even_generator()

### with generator comprehension:
# even_gen = (i for i in range(1, 10) if i % 2 == 0)

# print(type(even_gen))

# for item in even_gen:
# 	print(item)