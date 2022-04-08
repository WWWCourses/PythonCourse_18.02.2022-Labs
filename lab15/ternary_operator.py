# ----------------------- ternary operator in functions ---------------------- #
# ternary operator use case:
user_age = 13

# if user_age >= 18:
# 	status = 'adult'
# else:
# 	status = 'child'

status = 'adult' if user_age > 18 else 'child'
print(status)

# with function
def user_status(age):
	return 'adult' if age > 18 else 'child'

print(user_status(13))