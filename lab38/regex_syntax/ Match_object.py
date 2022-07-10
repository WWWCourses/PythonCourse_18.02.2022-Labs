import re

string = "price is: 1.234"
regex = re.compile('(\d+)\.(\d+)')

match = regex.search(string)

if match:
	print("match.group():", match.group())
	print("match.groups():", match.groups())
else:
	print("No match!")