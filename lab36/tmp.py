import re

string = 'ala bala'

matched = re.findall(r'a.*?a',string ) # greedy
print(matched)