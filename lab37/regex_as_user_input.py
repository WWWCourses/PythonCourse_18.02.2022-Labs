import re

rx_str = input('Enter a pattern:')
test_str = input('Enter a test string:')


m = re.search(rx_str, test_str)

if m:
	print(f'str:--->{test_str}<--- matched rx:--->{rx_str},<---')
else:
	print('No match')