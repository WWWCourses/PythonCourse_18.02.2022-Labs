import re

rx = re.compile(r'\bcat\b')
test_str = "kslk s cat ldsfslacat cat cat caterpilar cat"

replaced = rx.sub('DOG',test_str,count=1 )

print(replaced)