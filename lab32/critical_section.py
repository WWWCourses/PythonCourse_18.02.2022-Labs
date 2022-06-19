import threading
import time


def worker():
	# TODO: why counter not locked
	lock.acquire()
	global counter

	for i in range(10000000):
		counter += 1
	lock.release()



counter = 0

# create some treads to count together:
thread_pool = []
lock = threading.Lock()

for i in range(2):
	tr = threading.Thread(target=worker)
	thread_pool.append(tr)

	print(f"Counter before start of {tr.name}: {counter}")
	tr.start()

# wait for tread to finish:
for tr in thread_pool:
	tr.join()

print("Workers counted:", counter)