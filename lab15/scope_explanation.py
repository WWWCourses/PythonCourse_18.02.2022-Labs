# global scope
x = 1

def bar():
	x = 5
	def foo(z):
		# local scope:
		x = 9
		x += 1
		print(f'x in foo: {x}')

	foo(1)
	print(f'x in bar: {x}')

bar()
print(f'x in main: {x}')


# #namespaces
# Global = {
# 	'x': 00001,
# 	'bar':7f1f2656cdc0
# }

# deleted after line 15
# bar = {
# 	'x': 0003
# 	'foo': 98439598439
# }

# deleted after line  12
# foo = {
# 	'z': 00007
#   'x' : 00009
# }


# RAM:
# 	00001 => 1
#   7f1f2656cdc0 => <function bar>
#   0003  => 5
#   98439598439 => <functoin foo>
#   00007 => 1
#   00009=> 10







