# . Да се напише програма, която да намира медианата из между три стойности.
from statistics import median


try:
    number1 = int(input('Въведете число: '))
    number2 = int(input('Въведете число: '))
    number3 = int(input('Въведете число: '))

    mediana = 0

    if number3 < number1 < number2:
        mediana = number1

    elif number3 > number1 > number2:
        mediana = number1

    elif number1 < number2 < number3:
        mediana = number2

    elif number1 > number2 > number3:
        mediana = number2

    elif number1 < number3 < number2:
        mediana = number3

    elif number1 > number3 > number2:
        mediana = number3

    elif number1 == number2:
        mediana = number1

    elif number1 == number3:
        mediana = number1

    elif number3 == number2:
        mediana = number3

    else:
        mediana = number1

    print(mediana)
    print(median([number1, number2, number3]))

except ValueError:
    print('Въведете валидно число.')





