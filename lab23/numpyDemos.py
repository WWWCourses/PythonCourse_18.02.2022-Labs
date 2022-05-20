import numpy as np

# l = [1,2,3,4]

# a = np.array(l,dtype='int8')
# print(a)


# print(a.dtype)

# # create array of integers
# a = np.arange(1,10)

# # reshape
# a2d = a.reshape(3,3)
# print(a2d)

# print(a)
# a.resize(3,3)
# print(a)


# # shape of array
# print(a.shape)
# print(a2d.shape)

# # array dimensions
# print(a2d.ndim)

# a = np.zeros(100,dtype='int8')
# print(a)

# a = np.full((2,2), 4)
# print(a)

# a = np.linspace(0,100, 10, dtype='int8')
# print(a)

# a = np.arange(1,10).reshape(3,3)
# print(a)

# --------------------------------- indexing --------------------------------- #
l = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

a = np.array(l)

# print(l[1][2])
# print(a[1][2])# very very bad

# print(a[1,2])# the best way

# print(a[1])

# slicing
print( a[1:,1:])





