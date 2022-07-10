import re

# --------------------------------- example 1 -------------------------------- #
# rx_cat = re.compile(r'\bcat\b')
# rx_dog = re.compile(r'\bdog\b')

# rx = r'\bcat\b|\bdog\b'

# test_strings = [
# 	'this is cat!',  # match
# 	'this is catastrpoph!',  # no match
# 	'this is dog!',  # match
# 	'this is fish!',  # no match
# 	'the dog is hungry',  # match
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


# rx = re.compile(r'a(?:b|c)d')

# # (ab)|(cd) => 'ab',  'cd',
# # a(b|c)d  =>  'abd', 'acd'


# str = 'acd'

# m = rx.search(str)
# if m:
# 	print(f'{str} match')
# else:
# 	print(f'{str} no match')
