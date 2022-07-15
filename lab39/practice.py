import re

# ----------------------------------- TASK1 ---------------------------------- #
# Find the number of uppercase consonants (B,C,D,F,..,X,Y,Z) in a given string? E.g.: it should return 3 with the text ABcDeFO!. Note: Only ASCII. We consider Y to be a consonant! Example: the regex /./g will return 3 when run against the string abc.

# test_str = 'ABcDejfkjdkfdWssFO!' # 3
# rx = re.compile(r"(?=[A-Z])[^AIOEUY]")

# matched = rx.findall(test_str)
# print(f'Consonants count: {len(matched)}')




# ----------------------------------- TASK2 ---------------------------------- #
# For every occurence of the char #, match the previous character and save it in a group (backreference). Example: for the text "a#bc# -#", set backreferences with a, c and -. You are not allowed to consume the hash character.

# test_str = 'a#bc# -#' # 3
# rx = re.compile(r"(.)(?=#)")

# matched = rx.findall(test_str)
# print(matched)


# ----------------------------------- TASK3 ---------------------------------- #
# valid password must follow next rules:

# 1. Must contain at least one letter and digit
# 2. At least 8 characters long (any symbols are allowed)
# 3. Whitespaces is not allowed!

tests = [
	'a1234567',      # valid
	'a123 4567',     # not valid
	'123456789',     # not valid
	'123z4567',      # valid
	'a',			 # not valid
	'abcdabcdabcd',  # no number
	'abcdabcdabc1',  # valid
	'!!!!!!!!a1',  	 # valid
	'a1d2d3',  		 # no (<8)
]

rx = re.compile(r"^(?=.*[a-z])(?=.*\d)[^\s]{8,}$", re.I)

for test in tests:
	m = rx.search(test)
	if m:
		print(f'{test}: match')
