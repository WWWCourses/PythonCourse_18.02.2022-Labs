# TASK: sum of squares of 1 to 10_000_000 numbers:
# 333333383333335000000
# 333333383333335000000

import time
import threading as tr

def sum_squares(start, end):
	print('sum_squares')
	sum = 0
	for n in range(start, end+1):
		sum+= n**2

	return sum


start = 1
end = 15_000_000

# ------------------------------ sequential run ------------------------------ #
# start_time= time.perf_counter()

# sum1 = sum_squares(start,int(end/2))
# sum2 = sum_squares(int(end/2)+1,end)

# end_time= time.perf_counter()

# ------------------------------- threaded rnu ------------------------------- #
start_time= time.perf_counter()

# start this on Thread1:
# sum1 = sum_squares( start, int(end/2) )
tr1 = tr.Thread( target=sum_squares,  args=(start, int(end/2)))

# start this on Thread2:
# sum2 = sum_squares(int(end/2)+1,end)
tr2 = tr.Thread( target=sum_squares, args=(start,int(end/2)) )

tr1.start()
tr2.start()

end_time= time.perf_counter()

# print(sum1+sum2)
print(f'time taken: {end_time-start_time}')
