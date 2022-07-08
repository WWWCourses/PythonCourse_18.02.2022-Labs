import re
# ----------------------------------- Task1 ---------------------------------- #
# match string which starts with digit

# test_strings = [
# 	'', # no match
# 	'a123', # no match
# 	' 123', # no match
# 	'1a23', # match
# 	'1. dfkdsjfdkjgkf23', # match
# ]

# rx = re.compile(r'[0-9]')

# ----------------------------------- TASK2 ---------------------------------- #
# match valid user_name:
# 1. user_name must contains only letters, numbers and underscore,
# 2. user_name must be at least 3 symbols

# test_strings = [
# 	'', # no match,
# 	'a1', # no match (2)
# 	'a123', # match
# 	'12 3', # no match
# 	' 123', # no match
# 	'1a23', # match
# 	'1. dfkdsjfdkjgkf23', # match
# ]

# rx = re.compile(r'[a-zA-Z0-9_]{3,}')

# ----------------------------------- TASK3 ---------------------------------- #
# Split a string into words
test_strings = 'Matches Unicode word characters;this includes most characters that can be part of a word in any language,as well as numbers and the underscore.And so on... Turing1 best-friend a_b'


# words = test_strings.split(' ')

rx = re.compile(r'[a-zA-Z0-9_-]+')
rx = re.compile(r'[\w-]+')
words = rx.findall(test_strings)

for word in words:
	print(word)





# for str in test_strings:
# 	m = rx.search(str)
# 	if m:
# 		print(f"'{str}', # match'")
# 	else:
# 		print(f"'{str}, # no match'")


