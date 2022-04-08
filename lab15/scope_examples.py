def foo(x):
	x+=1 # x = x + 1
	print(f'x in foo: {x}')

x = 1

foo(x)
print(f'x in main: {x}')


# x in foo: 2
# x in main: 1