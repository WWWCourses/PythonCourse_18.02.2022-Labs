try:
	number = int(input('Enter a number [1000-9999]:'))
except:
	print('...Bye')
	exit()

if not (1000<=number<=9999):
	print('You did not enter a valid number in interval')
