import os

path = 'a/b/c/test.txt'

# normalize path
path_norm = os.path.normpath(path)
print(path_norm)

paths = path_norm.split(os.sep)

print(f'path_norm:{path_norm}')
print(f'paths:{paths}')

