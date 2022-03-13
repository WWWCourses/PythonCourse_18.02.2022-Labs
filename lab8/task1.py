#  Напишете програма, която чете цели числа въведени от потребителя и ги
# съхранява в списък. Програма трябва да продължи да чете стойности, докато
# потребителят не въведе 0.

numbers = []

x = int(input('Enter a number [0 for end]:'))
while x != 0:
	numbers.append(x)
	x = int(input('Enter a number [0 for end]:'))

sorted_numbers = sorted(numbers)

for num in sorted_numbers:
	print(num)



