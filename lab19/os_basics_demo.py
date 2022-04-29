import os

# print(os.name)
# print(os.uname().sysname)
# print(os.uname().machine)

cwd = os.getcwd()
# print(cwd)

# Set CWD:

# print(__file__)
print( os.path.realpath(__file__) )

os.chdir('/home/nemsys/projects/courses/netIT/PythonCourseNetIT/PythonCourse_18.02.2022-Labs/lab19/')


# print(os.listdir(path='/'))


absolute_file_path = '/home/nemsys/projects/courses/netIT/PythonCourseNetIT/PythonCourse_18.02.2022-Labs/lab19/data/somefile.txt'

relative_file_path = './data/somefile.txt'

# print( os.path.isdir('./data') )
# print( os.path.isdir(relative_file_path) )

with open(relative_file_path) as f:
	print(f.read())
