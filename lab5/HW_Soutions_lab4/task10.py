# Напишете програма, която да изчислява възрастта на дадено куче в кучешки
# години. Забележка: За първите две години, една кучешка година е равна на 10.5 човешки.
# След това всяка следваща кучешка година се равнява на 4-ри човешки години.


try:
    years = int(input('Въведете човешки години: '))

    if 0 <= years <= 2:
        dog_age = years * 10.5
    else:
        dog_age = 21 + years * 4

    print(dog_age)




except ValueError:
    print('Въведете валидни години.')


