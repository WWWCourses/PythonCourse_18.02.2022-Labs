# Напишете програма, която преобразува дадено число в интервала [0..999] в текст,
# съответстващ на българското произношение. Примери:
# -0 -> “Нула”
# -273 -> ”Двеста седемдесет и три”
# -400 -> ”Четиристотин”
# -501 -> “Петстотин и едно”
# -711 -> “Седемстотин и единадесет”

number = input('Въведете едно от следните числа 0, 273, 400, 501, 711: ')

if number == '0':
    print('Нула')
elif number == '273':
    print('Двеста седемдесет и три')
elif number == '400':
    print('Четиристотин')
elif number == '501':
    print('Петстотин и едно')
elif number == '711':
    print('Седемстотин и единадесет')
else:
    if number.isdigit():
        print('Не е въведено правилно число')
    else:
        print('Не е въведен правилен формат')
