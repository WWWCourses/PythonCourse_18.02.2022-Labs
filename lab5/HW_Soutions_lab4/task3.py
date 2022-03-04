# Напишете програма, която намира най-голямото по стойност число, измежду три дадени числа.
x = 56
y = 102
z = -1

if x > y and x > z:
    print("x is the maximum number, its value is {}".format(x))
elif y > x and y > z:
    print("y is the maximum number, its value is {}".format(y))
else:
    print("z is the maximum number, its value is {}".format(z))