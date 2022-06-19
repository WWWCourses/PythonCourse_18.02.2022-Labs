import threading as tr
import time

def worker(x):
	thread_name = tr.current_thread().name
	print(f'1.Worker {thread_name} is started: x = {x}')
	# do something time consuming
	local_end = time.time()

	# TODO: why not summing...
	while (local_end - start)<2:
		local_end = time.time()

	print(f'2.Worker {thread_name} end')


# ------------------------------ sequential run ------------------------------ #
start = time.time()
worker(1)
worker(2)
end = time.time()
print(f'Sequential Time: {end-start}\n') #



# ------------------------------- threaded run ------------------------------- #
start = time.time()
tr1 = tr.Thread( target=worker, name="TR1", args=(1,) )
tr2 = tr.Thread( target=worker, name="TR2", args=(2,) )

tr1.start()
tr2.start()

tr1.join()
tr2.join()

end = time.time()
print(f'Threaded Time: {end-start}') #


print(f'3. Main thread {tr.current_thread().name} END')



