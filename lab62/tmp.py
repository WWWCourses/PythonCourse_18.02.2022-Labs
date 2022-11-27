import re

a = '(2009)'
rx = re.compile(r'(\d+)')
year =rx.search(a).group(1)


print(int(year))