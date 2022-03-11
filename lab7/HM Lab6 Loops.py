
# Задача 1. Да се напише програма, която да намира тези числа, които се делят на 7 и на 5, между 1500 и 2700.#

for num in range(1500,2701):
    if num%35 == 0:
        print(num)

#Задача 2. Да се състави програма, която ще изчисли сумата на 5, въведени от клавиатурата, естествени числа от интервала [10 ..5555].
# Вход: 1,2,3,4,5
# Изход: 15#

# Коментар -  Не работи в изисквания диапазон!#

num_row = input ('Enter 5 random integers between 10 to 5555 range separated by space: ')
print('\n')
numbers = num_row.split()
for num_row in range(len(numbers)):
    numbers[num_row] = int(numbers[num_row])
    num_row = int(num_row)
print("Sum = ", sum(numbers))

# Задача 3. Да се напише програма, която да създаде следният шаблон:

for i in range(1, 6):
    print (i*'*')
for i in range(4, 0, -1):
    print (i*'*')

# Задача 4. Да се напише програма, която да обръща буквите на дадена дума на обратно. Думата да бъде въведена от клавиатурата. Като за целта използвате цикъл.

str = input('Input a word to reverse: ')
for a in reversed(str):
    print(a, end='')

#Задача 5. Да се напише програма, която да намира броят на четните и нечетните числа от списък от цели числа.
#Вход: numbers = [1,2,3,4,5,6,7,8,9]
# Изход:
# Number of even numbers: 4
# Number of odd numbers: 5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers, odd_numbers = 0, 0
for i in numbers:
    if i % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1         
print("Even numbers in the list: ", even_numbers)
print("Odd numbers in the list: ", odd_numbers)

#Задача 6. Да се напише програма, която да принтира всички числа от 0 до 6, без да включва 3 и 6.
# Изход: 0 1 2 4 5

for i in range(0, 7):
    if i==3 or i==6:
        continue
    print (i,end='')

#Задача 7. Да се напише програма, която принтира редицата на Фибуначи между 0 и 50.
#Редицата на Фибуначи е: 0, 1, 1, 2, 3, 5, 8, 13, 21, … Всяко следващо число е сумата от
#предходните две. 

n = int(input("Enter the n terms: "))
n1, n2 = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer!")
elif n == 1:
    print("Fibonacci sequence upto",n,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while n2<50:
        print(n2,end=' ')
        n1,n2 = n2, n1+n2

# Задача 9. Да се напише програма, която принтира следният шаблон:
#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999

rows = 10
for i in range(rows):
    for j in range(i):
        print (i, end='')
    print('')


# Задача 11: Да се състави програма, която извежда всички цели числа от интервала [1-
# 50], които удовлетворяват проверка на следното условие:
# c^3 = a^2 + b^2

# Коментар: Решението е за питагоровата теорема, а не по условието!#

limit = int(input('Enter upper limit: '))
c = 0
m = 2
while (c<limit):
    for n in range(1, m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if (c>limit):
            break
        if (a==0 or b==0 or c==0):
            break
        print(a, b, c)
    m=m+1

# Задача 12. Да се състави програма, която извежда числов триъгълник изобразяващ
# следната последователност:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#1 2 3 4 5 6
#1 2 3 4 5 6 7
#1 2 3 4 5 6 7 8
#1 2 3 4 5 6 7 8 9

rows = 9
for i in range(1, rows+1):
    for j in range(1, i+1):
        print (j, end='')
    print('')

# Задача 14. Да се напише програма, която да генерира число на случен принцип и да
# подкани потребителя да познае това число. Да извежда следните стойности too low, too
# high, или exactly right, в случай, че потребителя е познал, или не числото.

# Коментар: изполван е import за Random генератор!#

import random
number = random.randint(1, 10)
player_name = input('What is your name? ')
number_of_guess = 0
print ('Ok, ' + player_name + 'I am guessing a number between 1 and 10: ')
while number_of_guess <5:
    guess = int(input())
    number_of_guess += 1
    if guess < number:
        print ('Your guess is too low!')
    if guess > number:
        print ('Your guess is too high!')
    if guess == number:
        print ('Perfect match!')
        break
if guess == number:
    print ('You guessed the number in ' + str(number_of_guess) + ' tries!')
else:
    print ('You did not guess the number. The number was ' + str(number))