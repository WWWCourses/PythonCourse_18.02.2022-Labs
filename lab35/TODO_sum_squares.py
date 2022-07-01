import multiprocessing
import time

# TASK: sum squares of numbers in interval: [1, 100_000_000]

def sum_squares(start, end, lock):
	proc_id = multiprocessing.current_process().name

	lock.acquire()
	sum = q.get() # sum = 128,q = ()

	for n in range(start, end+1):
		# sum+= n**2
		sum+=n

	q.put(sum) # q = (456)
	lock.release()

	print(f'proc_id: {proc_id}; start={start},end={end}; sum={sum}')



if __name__ == '__main__':
	# sum = 0
	q = multiprocessing.Queue()
	q.put(0) # q = (0)

	lock = multiprocessing.Lock()

	range_start = 1
	range_end = 100
	batch_count = 5
	batch_size = int(range_end/batch_count)

	start = range_start
	end = start+batch_size

	processes = list()

	time_start = time.time()

	for n in range(batch_count):
		pr = multiprocessing.Process(target=sum_squares, args=(start, end, lock), daemon=True)
		processes.append(pr)
		pr.start()

		start = end	+ 1
		end = end+batch_size

	for pr in processes:
		pr.join()

	time_end = time.time()

	print(f'Total time: {time_end - time_start}')

	# TODO: why not working correct
	print(f'Sum in {multiprocessing.current_process().name} = {q.get()}')


