# Task 1
# Да се напише if-конструкция, която проверява стойността на две целочислени променливи и разменя техните стойности, ако стойността на първата променлива е по-голяма от втората.

# x = 10
# y = 5
x = None
y = None
try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    if x > y:
        # print("{} is greater than {}".format(x, y))
        print(str(x) + " is greater than " + str(y))
        # temp = x
        # x = y
        # y = temp
        x, y = y, x
        print("y: {}".format(y))
        print("x: {}".format(x))
except:
    print("Error: Invalid input.")


