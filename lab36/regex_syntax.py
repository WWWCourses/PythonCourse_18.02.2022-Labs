import re


# -------------------------------- Quantifiers ------------------------------- #
# rx = re.compile(r'1a?1')

# # 1a?1 =>'11', '1a1'
# # 1a*1 => '11', '1a1', '1aa1', ..., 1a...a1'
# test_str = '1aaa1'

# if rx.search(test_str):
# 	print('Match')
# else:
# 	print('No Match')

matched = re.search(r'a.*a','ala bala' );
print(matched)

