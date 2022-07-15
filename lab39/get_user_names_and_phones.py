import re

rx = re.compile(r"^(?P<name>[a-zA-Z]+)\s*:\s*(?P<tel>0[7-9]{2}\d{8})$", re.MULTILINE)
str_test = '''
maria: 08812345678
pesho :07722233344
pesho :07722233344 ldskflskls # no
pesho:066222333444  # no
pesho 232: 077222333444 #no

'''

matched = rx.findall(str_test)
user_data = dict()

if matched:
	for el in matched:
		user_data[el[0]] = el[1]
else:
	print('no match')

print(user_data)