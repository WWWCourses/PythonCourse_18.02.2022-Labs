x = None
print(type(x))

def userInput():
	while True:
		try:
			x = int(input('Enter an integer:'))
		except:
			print('AN INTEGER!!!')

		if x =='':
			break


userInput()