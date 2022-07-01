def sum_squares(start, end):
	sum = 0
	for n in range(start, end+1):
		# sum+= n**2
		sum+=n

	return sum


print(sum_squares(1, 101))
