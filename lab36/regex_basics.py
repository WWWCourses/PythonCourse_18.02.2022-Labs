import re

# --------------------------------- exmaple 1 -------------------------------- #
# pattern = "a\\\\b"; # a\\b
# print(pattern)

# # do the test:# match = re.search(pattern,str)

# rx = re.compile(r"a\\b")
# match = rx.search(str)

# if match:
# 	print('Match')
# else:
# 	print('No match')

# -------------------------- match multiple regexes -------------------------- #
test_string = '\\stop'

patterns = [
  '\\stop', 	# no match
  '\\\\stop', 	# match
  r'\\stop' 	# match
]

for pattern in patterns:
  if re.match(pattern, test_string):
    print(f"Pattern /{pattern}/ MATCHED string {test_string}!")
  else:
    print(f"Pattern /{pattern}/ DID NOT MATCHED string {test_string}!")
