# потребителя си възвежда година на раждане

# ако е пълнолетен => 'Welcome',
# else => 'Елате след X години', X = 18 - (2022 - 2010)

try:
	user_birth_year = int(input('Enter your birth year:'))
except:
	print('You did not anter a number! Bye!')


# проверка дали годината е валидна стойност (1900 - 2020)


if user_birth_year<1900 or user_birth_year>2020:
	print('You did not anter a valid year! Bye!')
	exit()


# hardecoded value for year is a bad practice
user_age = 2022-user_birth_year

if user_age<18:
	print(f'Елате след {18-user_age} години')
else:
	print('Welcome')

