import re
# ----------------------------------- flags ---------------------------------- #
pattern = r"""
a 	# match a
.+  # match all symbols, including \n when re.S is on
a   # match a
"""

rx = re.compile(pattern, re.I|re.S|re.X)
# rx = re.compile(r'(?si)a.+a')
test_str = '''A kjfkdsjk
fdsA'''

m = rx.findall(test_str)

if m:
	print(m)
else:
	print('no')