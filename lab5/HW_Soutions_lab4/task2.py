# Напишете програма, която показва знака (+ или -) от частното на две реални числа, без да го пресмята.

try:
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    if (x >= 0 and y >= 0) or (x < 0 and y < 0):
        print("+")
    elif (x >= 0 and y < 0) or (x < 0 and y >= 0):
        print("-")
except ValueError as err:
    print(err)



