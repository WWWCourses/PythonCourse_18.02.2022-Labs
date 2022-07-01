l = [1,2,3,4,5]

# list comprehension
# l_square = [el**2 for el in l]

# map function
def foo(el):
	return el**2


l_square = list(map(lambda el:el**2 ,l))


print(l_square) # [1,4,9,16,25]