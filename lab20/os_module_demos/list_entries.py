import os


print(os.getcwd())

def find_files(folder):
	entries = os.listdir(folder)
	for entry in entries:
		path = os.path.join('test',entry)
		if os.path.isdir(path):
			# print(f'{path} is Folder')
			find_files(path)
		else:
			print(f'{path} is File')


find_files('test')


