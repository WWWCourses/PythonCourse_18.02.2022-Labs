# x = 1

# l = ['Ada', 23] # Python: List, Others: Array

# del l[2]
# user_age = l.pop(2)
# print(l)

# Python: Dictionary; JS: object, PHP:assosiative array (hash array)
# d = {
# 	'name':'Ada',
# 	'age':23,
# }

# # Access dictionary values
# # read:
# print( d['age'] )
# # write:
# d['age']=50

# d['name'] = d['age']

# Add new dictionary element
# d = {
# 	'name':'Ada',
# 	'age':23,
# }

### change key:
# key = 'age'
# d['user_age'] = d[key]
# del d[key]
# print(d)

# print('name' == 'Name')
# name = d.pop('Name',None)
# print(name)

# clear dict:
# d = {
# 	'name':'Ada',
# 	'age':23,
# }

# # d = {}
# d.clear()

# print(type(d))

### popitem
# d = {
# 	'name':'Ada',
# 	'age':23,
# }

# age = d.popitem()
# print(d,age)


### copy dict:
# d = {
# 	'name':'Ada',
# 	'age':23,
# }

# this is not a copy
# backup = d
# d['age'] = 50

# this is a copy:
# backup = d.copy()
# d['age'] = 50

# print(d)
# print(backup)


# d = 3
# backup = d
# d = 9

# print(backup) # ?


# RAM:
# 			3244343=> 3
# 	backup:/
# 	d:		3244343 =>9

# ## sort dict keys:
# d = {
# 	'name':'Ada',
# 	'age': 23,
# }

# sorted_keys = sorted(d, reverse=True)
# print(sorted_keys)

# for key in sorted_keys:
# 	print(f'{key} - {d[key]}')

from re import L


user = {
	'name':'Ada',
	'age': 23,
}
# print( user.keys() )

### loop on dict keys:
# for key in user.keys():
# 	print(f'{key} - {user[key]}')


### loop on dict values:
# print( user.values() )
# for val in user.values():
# 	print(val)

### loop on dict keys,values (items):
# print( user.items() )

for key, value in user.items():
	# value = user[key]
	print(f'{key} - {value}')












