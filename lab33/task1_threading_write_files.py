# create function write_to_file(filename), which will create a file 200MB with symbol 'a'
# tip: 200MB = 200*1024*1025 byte


import time
import threading

def write_to_file(filename, symbol, length):
	with open(f'{filename}', "w") as ffw:
		ffw.write(symbol*length)
		# for i in range(length):
		# 	ffw.write(symbol)



len=200*1024*1024
start=time.time()
treads_pool=[]

## Sequential solution
for k in range(5):
	write_to_file(f'ffw{str(k)}.txt', 'z', len)

## Solution with treads:
for k in range(5):
	tr = threading.Thread(target=write_to_file, args=('ffw' + str(k) + '.txt', 'a', len))
	treads_pool.append(tr)

for k in range(5):
	treads_pool[k].start()
	treads_pool[k].join()

end=time.time()
print(f'Time taken: {end-start}')

