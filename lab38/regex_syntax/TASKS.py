import re
# ----------------------------------- TASK2 ---------------------------------- #
# match valid user_name:
# 1. user_name must contains only letters, numbers and underscore,
# 2. user_name must be at least 3 symbols
# 3. user_name must start with letter

test_strings = [
	'', 		 # no match,
	'a1', 		 # no match (2)
	'a123', 	 # match
	'ada', 	 	 # match
	'@ada', 	 # no match
	'ada!22222', # no match
	'1a23', 	 # no match
	'1_23', 	 # no match
]

rx = re.compile(r'^[a-zA-Z]\w{2,}$')


for str in test_strings:
	m = rx.search(str)
	if m:
		print(f'{str} match')
	else:
		print(f'{str} no match')


