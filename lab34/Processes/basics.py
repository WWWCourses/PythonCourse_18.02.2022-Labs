import multiprocessing
from re import X
import time

def worker():
	# global x
	# x+=1

	x = q.get()
	y = q.get()
	print(x,y)
	x+=1

	q.put(x)


	print(f'X in {multiprocessing.current_process().name} = {x}')


if __name__ == '__main__':
	# x = 0
	q = multiprocessing.Queue()
	q.put(0)

	for n in range(5):
		pr = multiprocessing.Process(target=worker)
		pr.start()




