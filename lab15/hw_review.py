#                                  Лекция 12 Функции задачи


# Задача 1. Да се напише функция, която да търси в списък. Като параметър да приема
# списък и да принтира ако елементът е в списъка неговата позиция, ако ли не да
# принтира, че не е намерен.


# def get_list():
# 	input_list = list()
# 	while True:
# 		element = input("Please provide an element for the list: ")
# 		if element == "":
# 			break

# 		input_list.append(element)

# 	return input_list

# def get_search_element():
# 	el = input("Please provide your search: ")
# 	return el

# def search_list(list_to_search, element_to_search):
# 	if element_to_search in list_to_search:
# 		return list_to_search.index(element_to_search)
# 	else:
# 		print(f"{element_to_search} not found.")

# 	# return list_to_search.index(element_to_search) if \
# 	# 	element_to_search in list_to_search \
# 	# 	else print(f"{element_to_search} not found.")

# l1 = get_list()
# search_element = get_search_element()
# res = search_list(l1, search_element)

# res = search_list([1,2,3], 4)
# print(res)


# Задача 2. Да се промени горната задача така, че тя да връща стойност и след това да се
# принтира резултатът в зависимост от върната стойност от функцията. Да се напише и
# още една функция, която да принтира резултатът от търсенето.
# Вход: [1, 2, 5, 9, 10], 5 Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2 Изход: Not found
#

def is_element_in_list(list_to_search, element_to_search):
	return True if element_to_search in list_to_search else False

def print_result(result):
	print('~' * 20)
	print(result)
	print('~' * 20)

list_to_search = [1,2,3]
search_element = 5

if __name__ == '__main__':
	if is_element_in_list(list_to_search,search_element):
		res = f'Position {list_to_search.index(search_element)}'
	else:
		res = 'Not Found'

	print_result(res)



# Задача 3. Да се напише програма, която да пита потребителя да въведе едно число от
# клавиатурата и да покаже съответното число от редицата на Фибoначи. Задачата да се
# реши с рекурсивна функция.


# n = int(input("Please provide a number: "))
#
#
# def calc_Fiboncci(n):
#     if n in {0, 1}:
#         return n
#     return calc_Fiboncci(n - 1) + calc_Fiboncci(n - 2)
#
#
# result = calc_Fiboncci(n)
# print(f"Number {n} in the Fibonacci sequence is {result}.")


# Задача 4. Да се напише програма, която да пита потребителя да въведе число от
# клавиатурата и да пресметне факториелът на това число. Да се използва рекурсия.


# n = int(input("Please provide a number: "))
#
#
# def calc_Factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * calc_Factorial(n - 1)
#
#
# result = calc_Factorial(n)
# print(f"The factorial of {n} is {result}.")


# Задача 5. Да се създаде програма, която да реализира няколко функции: добавяне (Add),
# изтриване (Remove), изтриване на всичко (clear), показване (show), край на програмата
# (Quit). Програмата да реализира програмна логика за количка за пазаруване (като тези
# в онлайн магазините). Потребителят да въвежда от клавиатурата даден елемент, след
# което да има възможност да го добави, изтрие, да види какво е поръчал.


# basket = []
#
#
# def add():
#     product = input("Please provide the name of the product you would like to put in your basket: ")
#     basket.append(product)
#
#
# def remove():
#     remove_product = input("Provide the name of the product to be removed from your basket: ")
#     basket.remove(remove_product)
#
#
# def clear():
#     basket.clear()
#
#
# def show():
#     print(basket)
#
#
# def shopping():
#     while True:
#
#         choice = int(input('''What would you like to do:
# #          press 1 for  product,
# #          2 for remove product,
# #          3 for clear the basket,
# #          4 to see the basked,
# #          5 to quit: '''))
#         if choice == 1:
#             add()
#         elif choice == 2:
#             remove()
#         elif choice == 3:
#             clear()
#         elif choice == 4:
#             show()
#         elif choice == 5:
#             print("Thank you for shopping.")
#             break
#         else:
#             print("Please provide a valid number.")
#
#
# shopping()


# Задача 6. Да се напише програма, която да сортира списък от tuples използвайки
# Lambda


# t = [(1, 2), (5, 6), (3, 4)]
#
# t.sort(key=lambda x: x[1])
# print(t)


# Задача 7. Да се напише програма, която да сортира списък от речници използвайки
# Lambda.


# d = {1: 2, 5: 6, 3: 4}
#
# d_new = dict(sorted(d.items(), key=lambda x: x[0]))
# print(d_new)


# Задача 8. Да се напише програма, която да намира сечението на два списъка
# използвайки lambda.


# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [5, 6, 7, 8, 9]
#
#
# intersection = (list(filter(lambda x: x in l1, l2)))
# print(intersection)


# Задача 9. Да се напише програма, която да брои четните и нечетните числа в даден
# списък от цели числа, използвайки lambda.

# l = [1, 2, 3, 4, 5, 6, 7]
#
# count_even = list(filter(lambda x: (x%2 == 0), l))
# print(len(count_even))
#
# count_odd = list(filter(lambda x: (x%2 != 0), l))
# print(len(count_odd))