# ------------------------------ copy by value: ------------------------------ #
# x = 5 # immutable

# def foo(n):
# 	# print(id(n))
# 	# n = 5
# 	n = 10
# 	# print(id(n))
# 	print(f'x in foo: {x}')
# 	print(f'n in foo: {n}')

# foo(x)
# print(id(x))
# print(x)

# RAM:
# 	x => 5
# 	n => 10


# ---------------------------- copy by refference ---------------------------- #
x = [5] # mutable

def foo(n):
	print(id(n))
	n[0] = 10
	print(id(n))
	print(f'x in foo: {x}')
	print(f'n in foo: {n}')

foo(x)
print(id(x))
print(x)
