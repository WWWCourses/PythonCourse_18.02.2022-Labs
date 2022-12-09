def foo(x):
	print(f'Foo x: {x}')
	return lambda x: print(f'Lambda: {x}')

foo(1)(9)
