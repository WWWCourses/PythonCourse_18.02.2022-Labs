from multiprocessing import Pool

def sum_squares(args):
	start, end = args
	return sum(range(start,end+1))

if __name__ == "__main__":
	n = 100
	procs = 5

	batch_size = int(n/procs)

	# Create size segments list
	jobs = []
	for i in range(procs):
		start = i*batch_size+1
		end = (i+1)*batch_size
		jobs.append((start,end) )

	pool = Pool(procs).map(sum_squares, jobs)
	result = sum(pool)
	print(f'result: {result}')