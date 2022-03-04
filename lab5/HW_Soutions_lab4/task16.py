month = "May"
nights = 15

if month == "May" or month == "October":
    studio = 50
    apartment = 65

    studio = studio * nights
    apartment = apartment * nights

    if nights > 14:
        studio *= 0.70
        apartment *= 0.90
    elif nights > 7:
        studio *= 0.95
elif month == "June" or month == "September":
    studio = 75.20 * nights
    apartment = 68.70 * nights

    if nights > 14:
        studio *= 0.80
        apartment *= 0.90
elif month == "July" or month == "August":
    studio = 76 * nights
    apartment = 77 * nights

    if nights > 14:
        apartment *= 0.90
print("Apartment: {:.2f}".format(apartment))
print("Studio: {:.2f}".format(studio))
