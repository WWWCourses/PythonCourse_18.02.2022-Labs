# ---------------------------------- TASK1: ---------------------------------- #
# match strings containing BG phone numbers: +359 DDDDDDDD
# import re

# rx = re.compile(r'\+359 [0-9]{8}')

# test_strings = [
# 	'+355 12345678', 	# no match
# 	'+359 12345678', 	# match
# 	'+359 1234 5678', 	# no match
# 	'+359 11111111', 	# match
# ]

# for test_str in test_strings:
# 	m = rx.search(test_str)
# 	if m:
# 		print('match')
# 	else:
# 		print('no match')

# ---------------------------------- TASK 2 ---------------------------------- #
# match consequence of 3 upper case cyrillic letters
# import re

# rx = re.compile(r'[А-Я]{3}')

# test_strings = [
# 	'abc', 				# no match
# 	'AGF', 				# match
# 	'АБЦ', 				# no match
# ]

# for test_str in test_strings:
# 	m = rx.search(test_str)
# 	if m:
# 		print('match')
# 	else:
# 		print('no match')

# --------------------------- TASK3 valis user name -------------------------- #
# sequence of at least 2 symbols: lower latin letters or numbers
import re

rx = re.compile(r'[a-z0-9]{2,}')

test_strings = [
	'ala bala', 		# no match
	'ala1bala', 		# match
	'a', 				# no match
	'324343',           # match
	'Ala'               # no match
]

for test_str in test_strings:
	m = rx.search(test_str)
	if m:
		print(m)
	else:
		print('no match')



# ---------------------------------- TASK 4---------------------------------- #
# ------------------------- Match valid email address ------------------------ #

# 32443232+2@gmail.com