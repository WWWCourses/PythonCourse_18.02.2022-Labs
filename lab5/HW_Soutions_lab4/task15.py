#
# try:
#     budget = float(input('Въведете бюджет: '))
#     category = input('Въведете категория: ')
#     people = int(input('Въведете запалянковци: '))
#     if people in range(1,5):
#         budget = budget - budget * 0.75
#     elif people in range(5,10):
#         budget = budget - budget * 0.60
#     elif people in range(10,25):
#         budget = budget - budget * 0.50
#     elif people in range(25,50):
#         budget = budget - budget * 0.40
#     elif people >= 50:
#         budget = budget - budget * 0.25
#     if category.upper() == 'VIP':
#         budget = budget - (people * 499.99)
#     elif category.lower() == 'normal':
#         budget = budget - (people * 249.99)
#     if budget >= 0:
#         print(f'Yes! You have {budget:.2f} leva left.')
#     else:
#         print(f'Not enough money! You need {budget*-1:.2f} leva.')
# except:
#     print('Въведете валидни данни!')


month = input("Моля, въведете желан месец на престой?- May, June, July, August, September or October: ")
number_of_nights = int(input("Моля, въведете брой нощувки? от 0 до 20: "))

if number_of_nights in range(1, 7):
    if month == "May" and "October":
        apartment = 65 * number_of_nights
        studio = 50 * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif month == "June" and "September":
        apartment = 68.70 * number_of_nights
        studio = 75.20 * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif month == "July" and "August":
        apartment = 77 * number_of_nights
        studio = 76 * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
elif number_of_nights in range(7, 15):
    if month == "May" and "October":
        discount = 0.05
        apartment = 65 * number_of_nights
        studio = (50 - 50*discount) * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif month == "June" and "September":
        apartment = 68.70 * number_of_nights
        studio = 75.20 * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif month == "July" and "August":
        apartment = 77 * number_of_nights
        studio = 76 * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
elif number_of_nights in range(15, 21):
    if month == "May" and "October":
        apartment = (65 - 65*0.10) * number_of_nights
        studio = (50 - 50*0.30) * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif month == "June" and "September":
        apartment = (68.70 - 68.70*0.10) * number_of_nights
        studio = (75.20 - 75.20*0.20) * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif month == "July" and "August":
        apartment = (77.00 - 77.00*0.10) * number_of_nights
        studio = 76.00 * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)

if month == "May" or "October":
    if 14 > number_of_nights > 7 :
        discount = 0.05
        apartment = 65 * number_of_nights
        studio = (50 - 50 * discount) * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif number_of_nights >= 15:
        discount = 0.30
        studio = (50 - 50 * discount) * number_of_nights
        apartment = (65 - 65 * 0.10) * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif number_of_nights <= 7:
        apartment = 65 * number_of_nights
        studio = 50 * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)
elif month == "June" or "September":
    if number_of_nights >= 15:
        studio = (75.20 - 75.20 * 0.20) * number_of_nights
        apartment = (68.70 - 68.70 * 0.10) * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
    Цена за Студио: {studio:.2f} лева за целия престой. """)
    elif number_of_nights <= 14:
        studio = 75.20 * number_of_nights
        apartment = 68.70 * number_of_nights
        print(f"""Цена за Апартамент: {apartment:.2f} лева за целия престой.
Цена за Студио: {studio:.2f} лева за целия престой. """)