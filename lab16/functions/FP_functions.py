# Functionial Programming (FP)

# # #classic function defintion syntax:
# def add(x,y):
# 	return x+y

# # # lambda syntax
# addLamda = lambda x,y:x+y

# print( add(2,3) )
# print( addLamda(2,3) )

# x = 1
# print( type(x))
# print( type(add) )
# print( type(addLamda) )
# print( type(lambda x,y:x+y))


# n = 2
# f = lambda x: x!=n
# print( f(5) )


# -------------------------- filter function example ------------------------- # Variant 1:
# l1 = [1,2,3,5,3]
# n = 3
# l2 = list(set(l1))
# l2.remove(n)

# print(l2)

# Varint 2
# l1 = [1,2,3,5,3]
# n = 3
# l2 = list()

# for el in l1:
# 	if el!=n:
# 		l2.append(el)
# print(l2)

# # Variant 3 (List Comprehension)
# l1 = [1,2,3,5,3]
# n = 3
# l2 = [ el for el in l1 if el!=n]
# print(l2)

# Varaint 4 with filter
# l1 = [1,2,3,5,3]
# n = 3

# def foo(x):
# 	return x!=n
# l2 = list(filter( foo, l1))

# l1 = [1,2,3,5,3]
# n = 3
# l2 = list(filter( lambda x: x!=n, l1))
# print(l2)

# for el in filter( lambda x: x!=n, l1):
# 	print(el)

# print(l2)


# map letters to upperCase:
# # variant 1
# letters = ['a', 'b', 'c']
# upper_leters = [el.upper() for el in letters  ]
# print(upper_leters)

# # variant 2
# letters = ['a', 'b', 'c']
# upper_leters = map(lambda el:el.upper(), letters)
# print(list(upper_leters))

# task: generate list of upper cyrrilic letters
# cyrillic_letters = list()
# for code in range(1040, 1072):
#  	cyrillic_letters.append()(chr(code))

# cyrillic_letters = [ chr(code) for code in range(1040, 1072)]

# cyrillic_letters = map(chr, range(1040, 1072))

# print(list(cyrillic_letters))





