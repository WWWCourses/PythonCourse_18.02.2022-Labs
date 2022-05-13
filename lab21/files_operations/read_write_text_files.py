import encodings
import os
print(os.getcwd())

# ---------------------------- read from text file --------------------------- #
# filename ='./test_data/data.txt'

# # Variant 1
# f = open(filename, 'r')
# data = f.read()
# f.close()

# # Variant 2: with context manager
# with open(filename, 'r') as f:
# 	data = f.read()
# 	# no need to close file explicitely


# ---------------------------- write in text file ---------------------------- #
# filename ='./data.txt'
# lines = ('Line1\n','Line2\n','Line3')

# ## Variant 1
# # f = open(filename,'w')
# # f.writelines(lines)
# # f.close()

# # Variant 2: with context manager
# with open(filename, 'w') as f:
# 	f.writelines(lines)

# ---------------------------- append in text file ---------------------------- #
# filename ='./test_data/data.txt'
# lines = ('Line3\n','Line4\n','Line5')

# with open(filename, 'a') as f:
# 	f.writelines(lines)


# ------------------------------- encoding demo ------------------------------ #
# filename ='./test_data/data_coded_with_windows-1251.txt'

# with open(filename,'r',encoding='KOI8-R') as f:
# 	data = f.read()
# 	print(data)


# --------------------------- read from binary file -------------------------- #
# filename ='./test_data/picture1.jpg'

# with open(filename,'rb') as f:
# 	data = f.read()
# 	print(data)

# ---------------------- use the proper way to set paths --------------------- #
# filename ='test_data/test.txt'
filename = os.path.join('test_data','data.txt')
print(filename)

with open(filename, 'r') as f:
	data = f.read()
	# no need to close file explicitely
