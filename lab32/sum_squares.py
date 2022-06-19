# TASK: sum of squares of 1 to 15_000_000 numbers:
# 1125000112500002500000


import time
import threading as tr

def sum_squares(start, end):
	print('*********** sum_squares started **********')
	global sum

	for n in range(start, end+1):
		sum+= n**2


start = 1
end = 15_000_000


# ------------------------------ sequential run ------------------------------ #
sum = 0
start_time= time.perf_counter()

sum_squares(start,int(end/2))
sum_squares(int(end/2)+1,end)

end_time= time.perf_counter()

print(f'sequential total sum: {sum}')
print(f'sequential total time: {end_time-start_time}')


# ------------------------------- threaded run ------------------------------- #
sum = 0
start_time= time.perf_counter()

# create Thread1:
tr1 = tr.Thread( target=sum_squares,  args=(start, int(end/2)))

# create Thread2:
tr2 = tr.Thread( target=sum_squares, args=(int(end/2)+1,end) )

tr1.start()
tr2.start()

tr1.join()
tr2.join()

end_time= time.perf_counter()

print(f'threaded total sum: {sum}')
print(f'threaded total time: {end_time-start_time}')
