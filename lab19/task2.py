# Да се напише програма, която да намери всички всички файлове в дадена директория.

import os

print(os.getcwd())

current_dir='/media/nemsys/data/projects/courses/netIT/PythonCourseNetIT/PythonCourse_18.02.2022-Labs/lab19'



# print( os.path.isfile(current_dir+'/'+'tmp.py'))

entries = os.listdir(current_dir)

files = list()

for entry in entries:
	print(os.path.join(current_dir,entry))
	if os.path.isfile(os.path.join(current_dir,entry)):
		files.append(entry)


print('All file entries:\n',files)