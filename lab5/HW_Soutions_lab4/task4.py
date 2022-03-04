# Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името на цифрата на български език.
try:
    number = int(input("Enter a number"))
    if number == 1:
        print("{} -> {}".format(number, "Едно"))
    elif number == 2:
        print("{} -> {}".format(number, "Две"))
    elif number == 3:
        print("{} -> {}".format(number, "Три"))
    elif number == 4:
        print("{} -> {}".format(number, "Четири"))
    elif number == 5:
        print("{} -> {}".format(number, "Пет"))
    elif number == 6:
        print("{} -> {}".format(number, "Шест"))
    elif number == 7:
        print("{} -> {}".format(number, "Седем"))
    elif number == 8:
        print("{} -> {}".format(number, "Осем"))
    elif number == 9:
        print("{} -> {}".format(number, "Девет"))
    else:
        print("The number is not between 1 and 9.")
except ValueError as err:
    print(err)
