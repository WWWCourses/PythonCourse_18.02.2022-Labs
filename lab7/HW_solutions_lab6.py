# --------------------------------- Задача 4. -------------------------------- #
# Да се напише програма, която да обръща буквите на дадена дума на обратно.
# Думата да бъде въведена от клавиатурата. Като за целта използвате цикъл.

# s = input('enter some text: ')
# reversed_s = ''

# for char in s:
# 	reversed_s = char + reversed_s

# print(reversed_s)

# --------------------------------- Задача 5. -------------------------------- #
# Да се напише програма, която да намира броят на четните и нечетните числа
# от списък от цели числа.

# numbers = [1,2,3,4,5,6,7,8,9]

# even = 0
# odd = 0

# for num in numbers:
# 	if num%2==0:
# 		even += 1
# 	else:
# 		odd+=1

# print(f'Number of even numbers: {even}')
# print(f'Number of odd numbers: {odd}')

# --------------------------------- Задача 7. -------------------------------- #
# Да се напише програма, която принтира редицата на Фибуначи между 0 и 50.
# Редицата на Фибуначи е: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... Всяко следващо число е сумата от
# предходните две.


# num1 = 0
# num2 = 1

# for i in range(1000):
# 	print(num1, end=',')
# 	n = num1 + num2
# 	num1 = num2
# 	num2 = n


# a = 1
# b = 0
# print(b)
# # print(a)

# while a <= 50:
# 	print(a)
# 	c = b
# 	b = a
# 	a = c + b


# -------------------------------- Задача 11: -------------------------------- #
# Да се състави програма, която извежда всички цели числа от интервала [1-
# 50], които удовлетворяват проверка на следното условие:
# c^3 = a^2 + b^2

# for a in range(1,51):
# 	for b in range(1,51):
# 		for c in range(1,51):
# 			if c**3 == a**2 + b**2:
# 				print(f'Found result: {a}^2 + {b}^2 = {c}^3')


# -------------------------------- Задача 13. -------------------------------- #
# Да се състави програма, чрез която се извежда квадрат от цифри. Сумите от
# елементите на произволен ред или стълб са равни на 45.


# a = 0
# for i in range(10):
# 	count = 0
# 	for j in range(10):
# 		idx =j+i+1
# 		if idx < 10:
# 			print(idx, end=" ")
# 		else:
# 			idx = 0
# 			print(idx+count, end=" ")
# 			count += 1

# 	print('\n')

# Задача 14.
# Да се напише програма, която да генерира число на случен принцип и да
# подкани потребителя да познае това число. Да извежда следните стойности too low, too
# high, или exactly right, в случай, че потребителя е познал, или не числото.
# import random

# number = random.randint(0, 100)
# print(number)


# -------------------------------- Задача 15. -------------------------------- #
# Да се напише програма, която подканва потребителя да въведе число и
# програмата да провери дали то е просто или не.

number = 88
# brute force => 12/2, 12/3, 12/4, 12/5 ...
is_prime = True

if number == 1:
	is_prime == True
else:
	for i in range(2,number):
		if number%i == 0:
			is_prime = False
			break

if is_prime:
	print(f'the number {number} is prime!')





# -------------------------------- Задача 19. -------------------------------- #
# Да се напише програма, която приема като вход текст и обръща буквите от
# дясно наляво на само на думите, чиято дължина е нечетна, тези които са с четен брой
# си остават така като са.


s = 'Make sure uoy only esrever sdrow of ddo length'
# s += ' '
# word = ''
# output = ''

# for char in s:
# 	word += char
# 	if char == ' ':
# 		if (len(word)-1)%2 == 0:
# 			output+=word + ' '
# 		else:
# 			reversed_word = ''
# 			for l in word:
# 				reversed_word = l + reversed_word
# 			output+=reversed_word + ' '

# 		word = ''

# print(output)

# Make sure you only reverse words of odd length
#
# words = s.split(' ')
# output = ''

# for word in words:
# 	reversed_word = ''

# 	if len(word) % 2 == 0:
# 		output += word + ' '
# 	else:
# 		for l in word:
# 			reversed_word = l + reversed_word
# 			output += reversed_word + ' '

# print(output)



