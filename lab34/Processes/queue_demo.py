"""
FILO === LIFO === Stack
	First In Last Out
	1, 2, 3 => Stack =>  1,2,3

FIFO === Queue:
	First In First Out
"""
import multiprocessing

q = multiprocessing.Queue()
q.put(1) # q = (1)
q.put(2) # q = (2,1)

x = q.get() # 1
y = q.get() # 2

print(x,y)




# # Put in queue:
# for i in range(4):
# 	q1.put(i+1) # 4,3,2,1 => 1

# # Get from queue:
# for i in range(4):
# 	print(q1.get())







