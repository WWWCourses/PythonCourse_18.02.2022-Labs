# --------------------------------- Задача 6. -------------------------------- #
# Да се напише програма, която да реализира тълковен речник. Програмата да
# може да търси по въведена дума, като например, ако речникът е френско-английски, то
# речника да може да предостави по въведена английска дума, съответният й еквивалент
# на френски. Ако английската дума се среща в речникът няколко пъти, то резултатът да
# бъде записан в списък, който след това да бъде принтиран. Ако думата не съществува да
# се изведе празен списък.


# desired output
# d = {
# 	'apple':['ябълка'],
# 	'exаmlpe':['образец','модел']
# }


# ### admin part:
# bg_end_dict = dict()

# while True:
# 	user_input = input('Enter en bg couple (like: \'apple:ябълка\'):')

# 	# stop entering when user enters ''
# 	if not user_input:
# 		break

# 	en_word, bg_word = user_input.split(':')

# 	if en_word in bg_end_dict:
# 		bg_end_dict[en_word].append(bg_word)
# 	else:
# 		bg_end_dict[en_word] = [bg_word]


# ### TODO: user part
# print(bg_end_dict)


# -------------------------------- Задача 13. -------------------------------- #
# Да се напише програма, която да групира думи по броят на главните букви в
# тях. Резултатът да се запази в речник, чиито ключове трябва да са броят на главните букви, а стойностите списък с думите. Думите не трябва да се повтарят в списъка.

# given:
words = ["HaPPy", "mOOdy", "yum my", "mayBE"]

# desired output:
# upper_case_counts = {
# 	3: ['HaPPy'],
# 	2: ['mOOdy','mayBE'],
# 	0: ['yummy']
# }

# code = 0
# upper_case_count = 0
# upper_case_counts = dict()

# for word in words:

# 	for letter in word:
# 		code = ord(letter)
# 		if 65 <= code <= 90:
# 			upper_case_count+=1

# 	if upper_case_count in upper_case_counts:
# 		upper_case_counts[upper_case_count].append(word)
# 	else:
# 		upper_case_counts[upper_case_count] = [word]
# 		# print(count)

# 	upper_case_count = 0

# print(upper_case_counts)



