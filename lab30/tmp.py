


def foo(x):
	# x =
	x[0] -= 5
	print(f'Lives in function: {lives}\n')
	print(locals())

if __name__ == '__main__':
	lives = [10]

	foo(lives)

	print(f'Lives in function: {lives}\n') #


	print(globals())