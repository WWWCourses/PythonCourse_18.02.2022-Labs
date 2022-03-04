# Дадени са няколко цели числа. Напишете програма, която намира онези подмножества от тях, които имат сума 0.
# Примери:
# Ако са дадени числата {-2, -1, 1}, сумата на -1, и 1 е 0
# Ако са дадени числата {3, 1, -7}, няма подмножества със сума 0

try:
    numbers = input("Enter three numbers in this format {1, -1, 2}: ")
    replaced_brackets = numbers.replace("{","").replace("}", "") # 1, -1, 2} => 1, -1, 2
    list_numbers = replaced_brackets.split(", ")
    print(list_numbers)

    if len(list_numbers) == 3 and numbers.index("{") != -1 and numbers.index("}") != -1:
        first_number = int(list_numbers[0])
        second_number = int(list_numbers[1])
        third_number = int(list_numbers[2])
        print(type(first_number))

        if first_number + second_number == 0:
            print("The sum of {} and {} is {}.".format(first_number, second_number, 0))
        elif first_number + third_number == 0:
            print("The sum of {} and {} is {}.".format(first_number, third_number, 0))
        elif second_number + third_number == 0:
            print("The sum of {} and {} is {}.".format(second_number, third_number, 0))
        else:
            print("There is no a subset with sum 0.")
    elif replaced_brackets.replace(", ", "").replace(",", "").isdigit() or not numbers.isdigit():
        print("The input is not in an appropriated format.")
except ValueError as err:
    print(err)
