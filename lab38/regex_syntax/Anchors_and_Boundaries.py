import re
# ----------------------------------- example 1 ---------------------------------- #
# rx = re.compile(r'^$')

# test_strings = [
# 	'alabala',
# 	'^$',
# 	' ',
# 	'',			# MATCH
# 	'^'
# ]

# for str in test_strings:
# 	m = rx.findall(str)
# 	if m:
# 		print(f'{str} match')
# 	else:
# 		print(f'{str} no match')


# --------------------------------- example 2 -------------------------------- #
rx = re.compile(r'(?m)^\s')

str = """not ok			# no match
 ok  			# match
   ok  			# match
	ok
"""

m  = rx.search(str)
if m:
		print(f'match')
else:
	print(f'no match')

# ------------------------------- word boundary ------------------------------ #

# \b	Matches on word boundaries, i.e. between word(\w) and non-word(\W) characters.
# Note that the start and end of string are considered as non-word characters.

# \w => 'k'
# \W => '*'
# 'k*'


rx = re.compile(r'\b')

str = r'k*'

m  = rx.findall(str)
if m:
	print(m)
else:
	print(f'no match')