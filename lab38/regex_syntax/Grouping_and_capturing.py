import re

# ---- task: find 3 letters word, which starts and ends with same symbol ---- #

# rx = re.compile(r'^([a-z])[a-z]\1$')

# test_strings = [
# 	'ala',  		# match
# 	'alan',  		# no match
# 	'mala',  		# no match
# 	'blb',  		# match
# 	'bll',  		# no match
# 	'ccc'    		# match
# ]

# for str in test_strings:
# 	# m_cat = rx_cat.search(str)
# 	# m_dog = rx_dog.search(str)

# 	m  = rx.search(str)

# 	if m:
# 		print(f'{str} match')
# 	else:
# 		print(f'{str} no match')


# --------------------------------- example 2 -------------------------------- #
rx = re.compile(r'^([^@]+)@([a-z]+)\.([a-z]{2,5})$')

# valid email:
# <username>@<letters>.<letters{2,5}>
test_strings = [
	'ala@abv.bg',  		# match
	'ala@abvbg',  		# no match
	'@abv.bg',  		# no match
	'ala_abv.bg',  		# no match
	'1@a.dd',  			# match
]

for str in test_strings:

	m  = rx.search(str)

	if m:
		print(m.groups()[0])
	# else:
	# 	print(f'{str} no match')


