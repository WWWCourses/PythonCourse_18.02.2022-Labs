import time

def threading_Thread(target, args):
	print('threading_Thread started')
	print(target)
	time.sleep(2)
	target(args[0])

def foo(filename):
	print('foo started')
	print(filename)



threading_Thread(target= foo, args = ('test.txt',))

# threading.Thread(target=wrt_fl('ffw' + str(k) + '.txt', 'a', len))
