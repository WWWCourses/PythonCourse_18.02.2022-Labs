import threading
import time

def worker():
	sum = 0
	for n in range(1_000_000):
		sum += n**2

	time.sleep(3)


tr1 = threading.Thread(target=worker)
tr2 = threading.Thread(target=worker)

tr1.start()
tr2.start()