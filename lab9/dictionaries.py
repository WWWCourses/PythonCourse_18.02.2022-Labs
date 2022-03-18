from hashlib import new


user_list = ['Ada', 23]
# user_list.append('Bulgaria')

# print( user_list[1] )


# user_dict = {
# 	'name':'Ada',
# 	'age': 23
# }

# access dictionary elements:
# d[key]
# d.get(key)

# print( user_dict['country'] )
# print( user_dict.get('country','No country') )

# key = 'Name'
# print( user_dict[key])
# print( user_dict.get(key))

# d = {
# 	'a': 1,
# 	'b': True,
# 	'c': [1,2,3],
# 	'd': {'name':'Ada', 'age':23},
# 	'e': 'abcde'
# }


# ---------------------------- dictionary of lists --------------------------- #
# data = {
# 	'sports': ['baseball', 'hokey', 'football'],
# 	'mouvies': [],
# 	'artists':[]
# }


# new_film = 'Film1'

# data['mouvies'].append(new_film)
# print(data)

# sports = ['baseball', 'hokey', 'football']
# d = dict({'sports':sports})
# print(d)

# --------------------------- lists of dictionaries -------------------------- #
user1 = {
	'name':'Ada',
	'age': 23
}

user2 = {
	'name':'Maria',
	'age': 31
}

users = [ user1, user2]
print(users)
